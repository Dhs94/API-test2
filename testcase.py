import requests
import unittest
import json
from demo import RunMain
from mock_test import mock_test

class wdms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = RunMain()

    def test_01(self):
        url = "http://127.0.0.1:8081/api/accounts/login/"
        data = {
            "username": "admin",
            "password": "admin"
        }
        data = json.dumps(data)
        result = self.res.run_request('post', url, data)
        self.assertEqual(result['code'], 200)

    def test_02(self):
        url = "http://127.0.0.1:8081/api/accounts/logout/"
        request_data = {
            "username": "admin",
            "password": "admin"
        }
        response_data = {'code': 201}
        res = mock_test(self.res.run_request, response_data, 'post', url, request_data)
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()