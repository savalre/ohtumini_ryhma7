"""
Main module for flask app
"""
from flask import Flask
#Will be needed in future
#from flask import render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    """
    Main page
    No parameters
    Returns: html for front page (for use by flask)
    """
    return '<h1> Flask </h1>'
