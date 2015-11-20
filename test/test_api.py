import unittest, requests


class TestApi(unittest.TestCase):
    def test_api_get(self):
        response = requests.get('http://localhost:5000/api/latestprice')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], "application/json")
