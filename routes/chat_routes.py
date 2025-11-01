from flask import Blueprint, request, jsonify
from ai_hub.services.ollama_service import ask_ollama

chat_bp = Blueprint("chat", __name__)   # ✅ le nom n'est plus vide

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "")
    model = data.get("model", "mistral")

    if not prompt:
        return jsonify({"error": "Prompt manquant"}), 400

    # Forcer la réponse en français
    prompt = f"Réponds en français : {prompt}"

    reply = ask_ollama(model, prompt)
    return jsonify({"reply": reply})
