from flask import Blueprint, request, jsonify
from ai_hub.models.ChatHistory import db, ChatHistory  # importer ChatHistory
from ai_hub.models.User import User

user_router = Blueprint("user_router", __name__)

@user_router.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")  # idéalement hashé

    # Vérifier que l'utilisateur existe
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    # Mettre à jour les champs si fournis
    if name:
        user.name = name
    if email:
        user.email = email
    if password:
        user.password = password  # attention : hasher le mot de passe en production

    db.session.commit()

    return jsonify({"message": "Utilisateur mis à jour avec succès"}), 200

