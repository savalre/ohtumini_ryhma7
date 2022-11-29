"""
Creates a connection between the database and the Flask app
"""
from flask_sqlalchemy import SQLAlchemy
from app import app
from db.get_db_filepath import db_filepath

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + db_filepath
db = SQLAlchemy(app)
