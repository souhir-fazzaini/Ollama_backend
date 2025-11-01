from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

from ai_hub.models.ChatHistory import db


class User(db.Model):
    __tablename__ = "users"  # table users

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)         # nom complet
    email = Column(String(120), unique=True, nullable=False)  # email unique
    password = Column(String(200), nullable=False)     # mot de passe hashé
    created_at = Column(DateTime, default=datetime.utcnow)
