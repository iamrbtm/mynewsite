from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    connect = f"mysql://{getenv('DB_USERNAME')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"
    app.config["SQLALCHEMY_DATABASE_URI"] = connect

    Migrate(app, db, render_as_batch=True)
