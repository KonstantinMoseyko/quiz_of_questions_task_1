from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from core.models import Question, Session

session = Session()

question_app = Blueprint("question_app", __name__)

@question_app.route("/", endpoint="list")
def questions_list():
    questions = session.query(Question).all()
    return render_template("question/list.html", questions=questions)

@question_app.route("/<int:question_id>/", endpoint="details")
def question_detals(question_id):
    question = session.query(Question).filter_by(id=question_id).first()
    if question is None:
        raise NotFound
    return render_template("question/details.html", question=question)
