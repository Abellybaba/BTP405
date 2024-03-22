import http
import unittest
from http.server import HTTPServer
from server import SimpleHTTPRequestHandler
import http.client
import json
import threading

class TestServerGET(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_address = ('localhost', 8000)
        cls.server = HTTPServer(cls.server_address, SimpleHTTPRequestHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()
    

    def test_get_method(self):
        # Connect to the server and send a GET request
        connection = http.client.HTTPConnection(*self.server_address)
        connection.request('GET', '/')
        respone = connection.getresponse()

        # Read and Decode the response
        data = respone.read().decode()
        connection.close()

        #check That the resopnse as expected
        self.assertEqual(respone.status, 200)
        self.assertEqual(respone.reason, 'OK')
        self.assertEqual(respone.getheader('Content-Type'), 'application/json')

        # Parse the JSON data and verify the content
        respone_data = json.loads(data)
        self.assertEqual(respone_data, {'message': 'This is a GET request response'})
  
class TestServerPOST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_address = ('localhost', 8000)
        cls.server = HTTPServer(cls.server_address, SimpleHTTPRequestHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    def test_post_method(self):
        # Prepare data for the POST request
        post_data = {'key': 'value'}
        json_data = json.dumps(post_data)

        # Send a POST request to the server
        connection = http.client.HTTPConnection(*self.server_address)
        connection.request('POST', '/', body=json_data, headers={'Content-Type': 'application/json'})
        response = connection.getresponse()

        # Read and Decode the response
        data = response.read().decode()
        connection.close()

        # Check that the response status is as expected
        self.assertEqual(response.status, 200)
        self.assertEqual(response.reason, 'OK')
        self.assertEqual(response.getheader('Content-Type'), 'application/json')

        # Parse the JSON data from the response and verify the content
        response_data = json.loads(data)
        self.assertEqual(response_data, {'received': post_data})

    def test_invalid_json_post(self):
        # Send a POST request with invalid JSON data to the server
        invalid_json_data = 'invalid json'
        connection = http.client.HTTPConnection(*self.server_address)
        connection.request('POST', '/', body=invalid_json_data, headers={'Content-Type': 'application/json'})
        response = connection.getresponse()

        # Read and Decode the response
        data = response.read().decode()
        connection.close()

        # Check that the server responds with a 400 status code for invalid JSON
        self.assertEqual(response.status, 400)
        self.assertEqual(response.reason, 'Bad Request')
        self.assertEqual(response.getheader('Content-Type'), 'application/json')

        # Parse the JSON error response and verify the content
        error_response = json.loads(data)
        self.assertEqual(error_response, {'error': 'Invalid JSON received'})

      
if __name__ == '__main__':
    unittest.main()