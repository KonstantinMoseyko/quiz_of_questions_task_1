from flask import Flask, render_template

from core.models import models, database
from core.views import question_app
from core.api import api_app

models.Base.metadata.create_all(bind=database.engine)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# bluprints registration
app.register_blueprint(question_app, url_prefix="/question")
app.register_blueprint(api_app, url_prefix="/api")
