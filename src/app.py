"""
Main module for flask app
"""
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "to_be_hidden"
