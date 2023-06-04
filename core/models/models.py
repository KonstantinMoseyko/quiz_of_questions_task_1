from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from core.models import Base

class Question(Base):
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True)
    id_question = Column(Integer, nullable=False)
    question = Column(String(255), nullable=False, default="")
    answer = Column(String(255), nullable=False, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    