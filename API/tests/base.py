from unittest import TestCase
from flask import json
from API.webapp import app


class BaseTest(TestCase):
    

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()
    
    

    
    