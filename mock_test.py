# coding:utf-8
import requests
import json
from unittest import mock


def mock_test(mock_method, response_data, method, url, requst_data):
    data = json.dumps(requst_data)
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(method, url, data)
    return res
