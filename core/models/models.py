from datetime import datetime

from core.models import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(255), nullable=False, default="")
    answer = db.Column(db.String(255), nullable=False, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    