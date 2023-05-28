from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from core.models import db


class Question(db.Model):
    id = Column(Integer, primary_key=True)
    body_question = Column(String(255), nullable=False, default="")
    body_answer = Column(String(255), nullable=False, default="")
    dt_created = Column(DateTime, default=datetime.utcnow)
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    