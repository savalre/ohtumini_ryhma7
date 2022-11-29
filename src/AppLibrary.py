"""
Library file to be used by the robot-testing framework
"""
import requests
from db.init_db import init_db
from app import app
import repositories.citation_repository

cite_repo = repositories.citation_repository.default_citation_repository

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        with app.app_context():
            init_db()

    def clear_db(self):
        with app.app_context():
            cite_repo.clear_citations()
