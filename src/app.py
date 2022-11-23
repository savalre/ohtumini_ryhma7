from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
        return '<h1> Flask </h1>'