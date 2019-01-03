import requests
import json
from util.operate_json import OperateJson


class RunMain:

    def get_main(self, url, data=None, cookies=None):

        if cookies:
            # json()输出类型为dict
            res = requests.get(url=url, data=data, cookies=cookies, verify=False).json()
        else:
            res = requests.get(url=url, data=data, verify=False).json()
            # 输出类型为str
            # res = json.dumps(res, indent=2, sort_keys=True)
        return res

    def post_main(self, url, data, cookies=None):
        data = json.dumps(data)
        if cookies:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False).json()
        else:
            res = requests.post(url=url, data=data, verify=False).json()
        return res

    def put_main(self, url, data, cookies=None):
        data = json.dumps(data)
        if cookies:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False).json()
        else:
            res = requests.post(url=url, data=data, verify=False).json()
        return res

    def delete_main(self, url, data, cookies=None):
        data = json.dumps(data)
        if cookies:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False).json()
        else:
            res = requests.post(url=url, data=data, verify=False).json()
        return res

    def run_request(self, method, url, data=None, cookies=None):
        if method == 'get':
            res = self.get_main(url=url, data=data, cookies=cookies)
        elif method == 'put':
            res = self.put_main(url=url, data=data, cookies=cookies)
        elif method == 'delete':
            res = self.delete_main(url=url, data=data, cookies=cookies)
        else:
            res = self.post_main(url=url, data=data, cookies=cookies)
        return json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)

