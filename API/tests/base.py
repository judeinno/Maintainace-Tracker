from unittest import TestCase
from flask import json
from API.webapp import app


class BaseTestCase(TestCase):

    USER_LOGIN_DETAILS = (
        email='jude@gmail.com',
        password='12345'
    )

    USER_DETAILS = dict(
        firstname='jude',
        Surname='inno',
        contact='12345',
        password='12345'
    )
    
    USER_REQUESTS = dict(
         field='Electricity',subfield='buld', 
         request_type='The bulb blew', requst_status="Not yet approved"
    )

    def setUp(self):
        self.app = app('testing')
        sekf.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client

        self.test_user = self.create_user(dict(
        firstname='jude',
        Surname='inno',
        contact='12345',
        password='12345'
        ))

    def tearDown(self):
        self.app_context.pop()

    def create_user(self, data):
        return self.client.post(
            '/API/auth/register',
            data=json.dumps(data),
            content_type='application/json'
        )
    
    def login_user(self, username, password):
        return self.client.post(
            '/API/auth/login',
            data=json.dumps(dict(
                username=username
                password=password
            ))
            content_type='application/json'
        )

    def create_requests(self, data, token):
        return self.client.post(
            '/API/users/requests',
            data=json.dumps(data),
            headers=dict(
                content_type='application/json',
                Authorization=token
            )
        )
        
    def create_req(self, id, data, token):
        return self.client.post(
            '/API/users/requests/{}/request/'.format(id)
            data=json.dumps(data)
            headers=dict(
                content_type='application/json',
                Authorization=token
            )
        )
    def get_auth_token(self):
        response = self.login_user(self.USER_LOGIN_DETAILS['email'], self.USER_LOGIN_DETAILS['password'])
        data = json.loads(response.data.decode())
        return data['auth_token']
