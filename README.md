# RAG Football — Analyste Tactique ⚽

Pipeline RAG (Retrieval-Augmented Generation) pour l'analyse tactique football.

## Architecture

```
Query utilisateur
     ↓
[1. Retrieval] TF-IDF → top-k chunks pertinents
     ↓
[2. Augmentation] Injection du contexte dans le prompt
     ↓
[3. Generation] Claude génère une réponse ancrée dans les docs
```

## Stack technique

| Composant | Choix | Justification |
|-----------|-------|---------------|
| Embedding | TF-IDF (sklearn) | Local, transparent, baseline solide |
| Vector store | Matrice numpy + cosine similarity | Simple, contrôlable |
| Chunking | Sentence-aware + overlap | Évite la perte de contexte |
| LLM | Claude claude-sonnet-4-20250514 | Génération fiable |
| UI | Streamlit | Démo rapide |

## Lancer le projet

```bash
# 1. Installation
pip install -r requirements.txt

# 2. Interface CLI
export ANTHROPIC_API_KEY="sk-ant-..."
python3 src/cli.py

# 3. Interface web
streamlit run app.py
```

## Ajouter des documents

Ajouter des entrées dans `data/raw/tactical_docs.py` puis relancer avec `--reset-index`.

En production : remplacer TF-IDF par des embeddings neuronaux (OpenAI, Cohere, all-MiniLM).

## Structure

```
rag-sport/
├── data/
│   ├── raw/tactical_docs.py   ← documents source
│   └── index/                 ← index TF-IDF sérialisé
├── src/
│   ├── rag_pipeline.py        ← pipeline complet
│   └── cli.py                 ← interface CLI
├── app.py                     ← interface Streamlit
└── requirements.txt
```
