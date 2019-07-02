import requests
import json


class RunMain:

    def get_main(self, url, data=None, cookies=None):

        if cookies:
            # json()输出类型为dict
            res = requests.get(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
            # res = json.dumps(res, indent=2, sort_keys=True)
        return res

    def post_main(self, url, data, cookies=None):
        data = json.dumps(data)
        if cookies:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res

    def put_main(self, url, data, cookies=None):
        data = json.dumps(data)
        if cookies:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res

    def delete_main(self, url, data, cookies=None):
        data = json.dumps(data)
        if cookies:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
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
        res = res.json()
        return json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)






# url = "http://127.0.0.1:8081/api/delete/departments/"
#
# data = {"zoneNumber":1, "departmentCode":[2,3,4]}
# headers = {
#     'Cookie':'csrftoken=4316d7a887c49957b9f00dd4c13da67b; sessionid=867c459a3239280c97ac0e0f5ebfe624'
#     }
# r=RunMain()
# response = r.run_request('post',url,data,headers)

