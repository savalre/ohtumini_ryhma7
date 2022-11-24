from os import path
from flask_sqlalchemy import SQLAlchemy
from app import app

basedir = path.abspath(path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + path.join(basedir, 'database.db')
db = SQLAlchemy(app)

