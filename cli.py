"""
cli.py — Interface CLI interactive pour le RAG Football.
Usage : python3 src/cli.py [--api-key sk-ant-...]
"""

import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rag_pipeline import rag_query, ingest_documents

BANNER = """
╔══════════════════════════════════════════════════╗
║         RAG Football — Analyse Tactique          ║
║  Posez des questions sur la tactique, les stats  ║
║  et les systèmes de jeu des top clubs européens  ║
╚══════════════════════════════════════════════════╝
  Commandes : 'quit' pour quitter | 'debug' pour toggle verbose
"""

EXAMPLES = """
Exemples de questions :
  → Comment fonctionne le pressing d'Arsenal ?
  → Quels sont les principes défensifs de l'Inter Milan ?
  → Compare le système offensif de City et du Real Madrid
  → Qu'est-ce que le PPDA et quelles équipes ont le meilleur score ?
  → Comment Vinicius Jr s'intègre dans le système du Real ?
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", default=None, help="Clé API Anthropic")
    parser.add_argument("--reset-index", action="store_true", help="Réindexer les documents")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("ANTHROPIC_API_KEY")

    print(BANNER)
    if not api_key:
        print("⚠  ANTHROPIC_API_KEY non configurée → mode demo (affiche contexte uniquement)")
        print("   Lancer avec : python3 src/cli.py --api-key sk-ant-...\n")
    else:
        print(f"✓ API key configurée → génération Claude activée\n")

    # Ingestion
    print("Chargement de l'index...")
    ingest_documents(reset=args.reset_index)
    print(EXAMPLES)

    verbose = False
    print("Prêt. Tapez votre question :\n")

    while True:
        try:
            query = input("❓ > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAu revoir.")
            break

        if not query:
            continue
        if query.lower() in ("quit", "exit", "q"):
            print("Au revoir.")
            break
        if query.lower() == "debug":
            verbose = not verbose
            print(f"  [Debug mode : {'ON' if verbose else 'OFF'}]")
            continue

        print("\n⏳ Recherche...")
        result = rag_query(query, api_key=api_key, verbose=verbose)

        print(f"\n{'─'*55}")
        print(f"📊 {result['n_chunks']} chunks récupérés")
        print(f"{'─'*55}")
        print(result["answer"])
        print(f"{'─'*55}\n")


if __name__ == "__main__":
    main()
