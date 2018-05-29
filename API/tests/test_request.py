from unittest
from run import app
import json


class request(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_successful_request_fetch(self):
        input_data = dict(category='user', field='Electricity', subfield='buld', request_type='The bulb blew', requst_status="Not yet approved")
    expected_response_message = 'User {} can view all requests.'.format(input_data['username'])
    get_response = self.tester.get('api/auth/signup')


if __name__ == '__main__':
    unittest.main()
        