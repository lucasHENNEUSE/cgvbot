import os
from openai import OpenAI
from dotenv import load_dotenv
from sql import sauvegarder_echange
from datetime import datetime

# Charger la clé API
load_dotenv()
ma_cle = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=ma_cle)

print("Bienvenue dans le chatbot CGV.")
print("Tape ta question ou 'exit' pour quitter.")

contexte = """Tu es un assistant juridique expert en e-commerce.
Tu réponds aux questions sur les Conditions Générales de Vente (CGV) :
paiement, droit de rétractation, livraison, garanties, données personnelles, litiges.
Tes réponses doivent être claires, fiables, avec des références juridiques si possible.
Si tu ne sais pas, indique-le sans inventer."""

continuer = True
while continuer:
    question = input("\nTa question : ")

    if question.lower() == "exit":
        print("À bientôt.")
        continuer = False
    else:
        resultat = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": contexte},
                {"role": "user", "content": question}
            ]
        )

        reponse = resultat.choices[0].message.content
        print("\nRéponse :", reponse)

        # Enregistrement dans la base
        try:
            sauvegarder_echange(question, reponse, datetime.now(), 1)
            print("Échange enregistré dans la base de données.")
        except Exception as e:
            print("Erreur lors de l'enregistrement :", e)
