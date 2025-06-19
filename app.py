from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Cargar tu API Key desde las variables de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Servidor funcionando correctamente."

@app.route("/webhook", methods=["POST"])
def webhook():
    user_message = request.form.get("Body")
    sender = request.form.get("From")

    if not user_message or not sender:
        return jsonify({"error": "Faltan parámetros"}), 400

    # Generar respuesta desde GPT-4-turbo
    completion = client.chat.completions.create(
        model="gpt-4o",  # Puedes usar gpt-4o o gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Eres un asistente por WhatsApp para atención al cliente."},
            {"role": "user", "content": user_message}
        ]
    )

    response_text = completion.choices[0].message.content.strip()

    return jsonify({"respuesta": response_text}), 200


