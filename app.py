from flask import Flask
from .db import create_db, delete_db

app = Flask(__name__)


@app.route("/create-db")
def create_db_route():
    create_db()
    return "Just borked your repo brah..."


@app.route("/delete-db")
def delete_db_route():
    delete_db()
    return "Just deleted the DB"
