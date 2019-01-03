import requests
import json

class RunMain():
    def __init__(self):
        self.request = requests.session()
        # self.run = self.run_request(method, url, data)

    def send_get(self, url, data=None):
        # res = requests.get(url).json()
        res = self.request.get(url, data).json()
        return res


    def send_post(self, url, data):
        # res = requests.post(url, data).json()
        # json()输出类型为dict
        res = self.request.post(url, data).json()
        # 输出类型为str
        # res = json.dumps(res, indent=2, sort_keys=True)
        return res


    def run_request(self, method, url, data=None):
        if method == 'get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    run = RunMain()
    url = "http://127.0.0.1:8081/api/accounts/login/"
    data = {
        "username": "admin",
        "password": "admin"
    }
    data = json.dumps(data)
    print(run.run_request('post', url, data))
    url2 = "http://127.0.0.1:8081/api/accounts/logout/"
    requst_data = {
        "username": "admin",
        "password": "admin"
    }
    response_data = {}
    data2 = json.dumps(requst_data)
    print(run.run_request('post', url2, data2))