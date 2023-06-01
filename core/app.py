import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_migrate import Migrate

from core.models import db
from core.views import question_app
from core.api import api_app
from core import commands


load_dotenv()

app = Flask(__name__)
migrate = Migrate(app, db, compare_type=True, render_as_batch=True)

@app.route("/")
def index():
    return render_template("index.html")

# bluprints registration
app.register_blueprint(question_app, url_prefix="/question")
app.register_blueprint(api_app, url_prefix="/api")

# commands registration
app.cli.add_command(commands.init_db)

# configuration
cfg_name = os.getenv("CONFIG_NAME")
app.config.from_object(f"core.config.{cfg_name}")

# extensions registration
db.init_app(app)
