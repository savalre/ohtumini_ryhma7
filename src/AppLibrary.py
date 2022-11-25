"""
Library file to be used by the robot-testing framework
"""
import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

    def placeholder_should_pass(self):
        pass
