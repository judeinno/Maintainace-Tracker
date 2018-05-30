from flask import json
from API.tests.base import BaseTestCase

class TestCreateUser(BaseTestCase):
    def test_response_status(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 201) 
    def test_response_messages(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            data = json.loads(response.data.decode())
            self.assertTrue(data is not None)
            self.assertEqual(data['message'], 'User registration successful')

    def test_token_returned(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            data = json.loads(response.data.decode())
            self.assertTrue(data['auth_token'])
    def test_user_exists(self):
        with self.client:
            response = self.create_user(self.USER_DETAILS)
            self.assertEqual(response.status_code, 201)
            response = self.create_user(self.USER_DETAILS)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 403)
            self.assertEqual(data['message'], 'User already exists!')

class TestLogin(BaseTestCase):
    def test_response_status(self):
        with self.client:
            response = self.login_user(self.USER_LOGIN_DETAILS['username'], self.USER_LOGIN_DETAILS['password'])
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_response_messages(self):
        with self.client:
            response = self.login_user(self.USER_LOGIN_DETAILS['username'], self.USER_LOGIN_DETAILS['password'])
            data = json.loads(response.data.decode())
            self.assertEqual(data['message'], 'Successfully Logged in.')

    def test_token_returned(self):
        with self.client:
            response = self.login_user(self.USER_LOGIN_DETAILS['username'], self.USER_LOGIN_DETAILS['password'])
            data = json.loads(response.data.decode())
            self.assertTrue(data['auth_token'])