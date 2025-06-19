import openai
from flask import Flask, request, jsonify
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    user_message = data.get("Body")
    sender = data.get("From")

    if not user_message or not sender:
        return jsonify({"error": "Datos incompletos"}), 400

    # Llamar a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})




