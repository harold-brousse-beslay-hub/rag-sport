"""
app.py — Interface Streamlit pour le RAG Football.
Lancer : streamlit run app.py
"""

import streamlit as st
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from rag_pipeline import rag_query, ingest_documents

st.set_page_config(page_title="RAG Football", page_icon="⚽", layout="wide")

st.title("⚽ RAG Football — Analyste Tactique")
st.caption("Posez des questions sur la tactique, les stats et les systèmes des top clubs européens")

# Sidebar config
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Clé API Anthropic", type="password",
                             help="sk-ant-... — laissez vide pour le mode demo")
    reset_btn = st.button("🔄 Réindexer les documents")
    st.divider()
    st.subheader("📋 Exemples de questions")
    examples = [
        "Comment Arsenal presse haut ?",
        "Quelle est la tactique défensive de l'Inter Milan ?",
        "Explique le rôle de Bellingham au Real Madrid",
        "Qu'est-ce que le PPDA ?",
        "Compare l'attaque de City et du Bayern",
    ]
    for ex in examples:
        if st.button(ex, key=ex):
            st.session_state.query_input = ex

# Init index
@st.cache_resource
def get_index(reset=False):
    return ingest_documents(reset=reset)

if reset_btn:
    st.cache_resource.clear()
    st.success("Index réinitialisé !")

with st.spinner("Chargement de l'index..."):
    get_index()

# Main interface
col1, col2 = st.columns([3, 1])
with col1:
    query = st.text_input(
        "Votre question tactique",
        value=st.session_state.get("query_input", ""),
        placeholder="Ex: Comment fonctionne le pressing de Manchester City ?"
    )
with col2:
    ask_btn = st.button("🔍 Analyser", type="primary", use_container_width=True)

if ask_btn and query:
    with st.spinner("Analyse en cours..."):
        result = rag_query(query, api_key=api_key or None)

    st.subheader("📝 Réponse")
    st.write(result["answer"])

    with st.expander(f"📚 Contexte récupéré ({result['n_chunks']} chunks)", expanded=False):
        for c in result["chunks_used"]:
            meta = c["metadata"]
            label = meta.get("team") or meta.get("topic") or "général"
            st.markdown(f"**[{c['rank']}] {label}** — score: `{c['score']}`")
            st.text(c["text"])
            st.divider()
