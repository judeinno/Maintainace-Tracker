import unittest
from API import app
import json


class request(unittest.TestCase):
    def setUp(self):
        self.tester = app.app.test_client(self)

    def test_successful_request_fetch(self):
        input_data = dict(category='user', username='username', field='Electricity', subfield='buld', request_type='The bulb blew', requst_status="Not yet approved")
        get_response = self.tester.get('/user/requests')    
    
        self.assertEqual(get_response.status_code, 201)
        

    def test_successfully_create_request(self):
        input_data = dict(category='user', username='username', field='Electricity', subfield='buld', request_type='The bulb blew', requst_status="Not yet approved")
        get_response = self.tester.post('/user/requests', content_type='application/json', data=json.dumps(input_data))    
        
        self.assertEqual(get_response.status_code, 201)
        



if __name__ == '__main__':
    unittest.main()
        