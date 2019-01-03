import requests
import json
from util.operate_json import OperateJson
from Base.RunMethod import RunMain
from util.operate_excel import OperateExcel


class OperateHeader:

    # 获取 cookie
    def get_cookies(self, url, data):
        requests_data = json.dumps(data)
        cookies = requests.post(url, requests_data).cookies
        return cookies

    # 将cookie写入json文件
    def write_cookies(self, url, data):
        cookie_jar = self.get_cookies(url, data)
        # 转换成字典
        cookies = requests.utils.dict_from_cookiejar(cookie_jar)
        op_json = OperateJson()
        op_json.write_json(cookies)


