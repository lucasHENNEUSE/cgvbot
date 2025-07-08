# CGVbot

> Assistant juridique spécialisé dans les Conditions Générales de Vente (CGV), utilisable en ligne de commande. Ce projet a été réalisé dans le cadre d’un exercice pédagogique sur le fine-tuning d’un modèle OpenAI.

## Objectifs

- Répondre à des questions juridiques courantes relatives aux CGV
- S’appuyer sur un modèle GPT-4.1 nano fine-tuné
- Consigner les échanges dans une base SQLite via Docker
- Utilisation en ligne de commande (console Python)

## Technologies utilisées

- Python 3.10+
- OpenAI API (fine-tuning GPT-4.1 nano)
- SQLite (via `sql.py`)
- Fichier d’entraînement `.jsonl`
- Git / GitHub

## Lancer le projet

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
