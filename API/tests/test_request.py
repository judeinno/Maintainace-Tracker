import unittest
from API.webapp import app
import json
from flask_testing import TestCase


class request(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.client = app.test_client(self)

    def test_successful_request_fetch(self):
        with self.client:
            input_data = dict(category='user', username='username', field='Electricity', subfield='buld', request_type='The bulb blew', requst_status="Not yet approved")
            get_response = self.client.get('/user/requests')
            reply = json.loads(get_response.data.decode())

            self.assertEquals(reply["message"], "successfully fetched request")
            self.assertEqual(get_response.status_code, 201)
        

    def test_successfully_create_request(self):
        input_data = dict(category='user', username='username', field='Electricity', subfield='buld', request_type='The bulb blew', requst_status="Not yet approved")
        get_response = self.client.post('/user/requests', content_type='application/json', data=json.dumps(input_data))    
                    
        self.assertEqual(get_response.status_code, 201)
        



if __name__ == '__main__':
    unittest.main()
        