"""
rag_pipeline.py — Pipeline RAG football avec TF-IDF retrieval + Claude generation.
"""

import os, sys, pickle, numpy as np
from typing import List, Dict, Any, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import anthropic

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data", "raw")
INDEX_DIR = os.path.join(ROOT, "data", "index")
sys.path.insert(0, DATA_DIR)
from tactical_docs import get_all_documents

INDEX_FILE = os.path.join(INDEX_DIR, "tfidf_index.pkl")
TOP_K = 4
CHUNK_SIZE = 300
CHUNK_OVERLAP = 60


# ── 1. CHUNKING ───────────────────────────────────────────────────────────────

def chunk_text(text: str, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP) -> List[str]:
    sentences = [s.strip() for s in text.split("\n") if s.strip()]
    chunks, buf, buf_len = [], [], 0
    for sent in sentences:
        n = len(sent.split())
        if buf_len + n > chunk_size and buf:
            chunks.append(" ".join(buf))
            ob, ol = [], 0
            for s in reversed(buf):
                if ol + len(s.split()) > overlap: break
                ob.insert(0, s); ol += len(s.split())
            buf, buf_len = ob, ol
        buf.append(sent); buf_len += n
    if buf: chunks.append(" ".join(buf))
    return chunks


def build_chunks(docs: List[Dict]) -> Tuple[List[str], List[Dict]]:
    texts, metas = [], []
    for doc in docs:
        for i, chunk in enumerate(chunk_text(doc["text"])):
            texts.append(chunk)
            metas.append({
                "doc_id": doc["id"], "source": doc.get("source",""),
                "team": doc.get("team",""), "season": doc.get("season",""),
                "topic": doc.get("topic",""), "chunk_index": i
            })
    return texts, metas


# ── 2. INDEX TF-IDF ───────────────────────────────────────────────────────────

class TFIDFIndex:
    """Index TF-IDF avec persistance pickle."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer(ngram_range=(1,2), max_df=0.95, sublinear_tf=True)
        self.matrix = None
        self.texts: List[str] = []
        self.metas: List[Dict] = []

    def build(self, texts, metas):
        self.texts, self.metas = texts, metas
        self.matrix = self.vectorizer.fit_transform(texts)
        print(f"✓ Index : {len(texts)} chunks × {self.matrix.shape[1]} termes TF-IDF")

    def query(self, q: str, top_k=TOP_K) -> List[Dict]:
        q_vec = self.vectorizer.transform([q])
        scores = cosine_similarity(q_vec, self.matrix)[0]
        top_idx = np.argsort(scores)[::-1][:top_k]
        return [
            {"rank": r+1, "text": self.texts[i], "metadata": self.metas[i], "score": round(float(scores[i]),4)}
            for r, i in enumerate(top_idx) if scores[i] > 0
        ]

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f: pickle.dump(self, f)

    @staticmethod
    def load(path) -> "TFIDFIndex":
        with open(path, "rb") as f: return pickle.load(f)


def ingest_documents(reset=False) -> TFIDFIndex:
    if os.path.exists(INDEX_FILE) and not reset:
        print(f"✓ Index chargé depuis {INDEX_FILE}")
        return TFIDFIndex.load(INDEX_FILE)
    docs = get_all_documents()
    texts, metas = build_chunks(docs)
    print(f"  {len(docs)} docs → {len(texts)} chunks")
    idx = TFIDFIndex()
    idx.build(texts, metas)
    idx.save(INDEX_FILE)
    return idx


# ── 3. GENERATION ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """Tu es un analyste tactique football expert. Tu réponds en français.
Règles strictes :
- Tu utilises UNIQUEMENT les informations du contexte fourni.
- Si une info manque dans le contexte, dis-le clairement.
- Tu cites les métriques et chiffres du contexte.
- Réponses structurées, directes, sans rembourrage."""


def format_context(chunks: List[Dict]) -> str:
    parts = []
    for c in chunks:
        m = c["metadata"]
        label = m.get("team") or m.get("topic") or "général"
        parts.append(f"[{label} | score={c['score']}]\n{c['text']}")
    return "\n\n---\n\n".join(parts)


def generate_answer(query: str, chunks: List[Dict], api_key=None) -> str:
    api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
    if not chunks:
        return "Aucun document pertinent trouvé pour cette question."
    context = format_context(chunks)
    user_msg = f"Contexte disponible :\n{context}\n\n---\n\nQuestion : {query}"
    if not api_key:
        return f"[MODE DEMO — ANTHROPIC_API_KEY manquante]\n\nContexte injecté :\n{context[:600]}..."
    client = anthropic.Anthropic(api_key=api_key)
    resp = client.messages.create(
        model="claude-sonnet-4-20250514", max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[{"role":"user","content":user_msg}]
    )
    return resp.content[0].text


# ── 4. PIPELINE PUBLIC ────────────────────────────────────────────────────────

_CACHE: TFIDFIndex = None

def get_index() -> TFIDFIndex:
    global _CACHE
    if _CACHE is None: _CACHE = ingest_documents()
    return _CACHE


def rag_query(query: str, api_key=None, verbose=False) -> Dict[str, Any]:
    idx = get_index()
    chunks = idx.query(query, top_k=TOP_K)
    if verbose:
        print(f"\n{'═'*55}\nQuery : {query}\nChunks récupérés :")
        for c in chunks:
            label = c["metadata"].get("team") or c["metadata"].get("topic")
            print(f"  [{c['rank']}] {c['score']} | {label} | {c['text'][:70]}...")
        print(f"{'═'*55}\n")
    answer = generate_answer(query, chunks, api_key)
    return {"query": query, "answer": answer, "chunks_used": chunks, "n_chunks": len(chunks)}


if __name__ == "__main__":
    print("=== RAG Football – Test pipeline ===\n")
    idx = ingest_documents(reset=True)
    queries = [
        "Comment Arsenal utilise le pressing haut ?",
        "Quelles stats offensives pour Manchester City ?",
        "Système défensif Inter Milan",
    ]
    for q in queries:
        print(f"\nQ: {q}")
        for c in idx.query(q, top_k=2):
            label = c["metadata"].get("team") or c["metadata"].get("topic")
            print(f"  [score={c['score']}] {label} → {c['text'][:110]}...")
