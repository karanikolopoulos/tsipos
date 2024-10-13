
import os.path as osp

from . import db
from dataclasses import dataclass
from flask import Flask

DATABASE_PATH = osp.join("data", "database.db")

@dataclass
class Participant:
    first: str
    last: str
    mail: str

def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["DATABASE"] = DATABASE_PATH
    app.secret_key = "secret_key"
    
    db.init_app(app)
    return app