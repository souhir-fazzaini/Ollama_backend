from venv import logger

from flask import Blueprint, request, jsonify

from ai_hub.models.ChatHistory import ChatHistory, db

history_router = Blueprint("history_router", __name__)

@history_router.route("/history", methods=["POST"])
def save_history():
    data = request.json
    new_entry = ChatHistory(
        question=data["question"],
        answer=data["answer"]
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Historique enregistré"}), 201


@history_router.route("/history", methods=["GET"])
def get_history():
    history = db.session.query(ChatHistory).all()
    return jsonify([{
        "id": h.id,
        "question": h.question,
        "answer": h.answer,
        "created_at": h.created_at.isoformat()
    } for h in history])

@history_router.route("/stats", methods=["GET"])
def get_stats():
    total_entries = db.session.query(ChatHistory).count()
    total_messages = total_entries * 2

    # Récupérer la dernière activité (dernier enregistrement)
    last_entry = db.session.query(ChatHistory).order_by(ChatHistory.created_at.desc()).first()
    last_activity = last_entry.created_at.isoformat() if last_entry else None
    logger.info("last",last_activity)
    return jsonify({
        "total_conversations": total_entries,
        "total_messages": total_messages,
        "last_activity": last_activity
    })

