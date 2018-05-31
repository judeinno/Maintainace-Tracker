import unittest
from API.webapp import app
import json
from flask_testing import TestCase
from API.tests.base import BaseTest

class TestUserRequests(BaseTest):

	def test_if_URL_exists(self):
		response = self.client.get('/api/v1/users/requests/1')
		assert "200 OK" ==response.status

	def test_api_check_non_authorised_user(self):
		with self.client:
			response = self.client.get('/api/v1/users/requests/1')
			reply = json.loads(response.data.decode())
			self.assertEquals(reply["success"],False)
			self.assertEquals(reply["message"],"You are not authorised to access this page.")

	def test_api_check_request(self):
		with self.client:
			head={'Authorization':'123'}
			response = self.client.get('/api/v1/users/requests/1',headers = head)
			reply = json.loads(response.data.decode())
			self.assertEquals(reply,{'Field':'Electricity','SubField':'bulb','RequestType':'replace','RequestStatus':'Not yet approved'})

   