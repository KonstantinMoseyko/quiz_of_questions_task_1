from flask import Blueprint, jsonify, request
from datetime import datetime
import requests

from core.models import db, Question


api_app = Blueprint("api_app", __name__)

@api_app.route('/', methods=['POST'])
def jservice_request():
    data = request.get_json()
    questions_num = data.get('questions_num')
    
    while True:
        response = requests.get(f"https://jservice.io/api/random?count={questions_num}")
        data = response.json()

        for item in data:
            existing_question = db.session.query(Question).filter_by(id_question=item['id']).first()
            if existing_question is None:
                question = Question(
                    id_question=item['id'], 
                    question=item['question'], 
                    answer=item['answer'], 
                    created_at=datetime.fromisoformat(item['created_at'].replace('Z', '+00:00')),
                    updated_at=datetime.fromisoformat(item['updated_at'].replace('Z', '+00:00')),
                )

                db.session.add(question)

        if db.session.new:
            db.session.commit()
            break

    last_question = db.session.query(Question).order_by(Question.id.desc()).offset(1).first()

    db.session.close()

    if last_question is not None:
        result = {
            'id_question': last_question.id_question,
            'question': last_question.question,
            'answer': last_question.answer,
            'created_at': last_question.created_at,
            'updated_at' : last_question.updated_at
        }
    else:
        result = {}

    return jsonify(result)
