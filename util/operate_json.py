import json


class OperateJson:

    def __init__(self, path=None):
        if path:
            self.file_path = path
        else:
            self.file_path = r"../dataconfigure/data.json"
        self.data = self.read_data()

    # 读取json文件数据
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
        return data

    # 获取关键字数据
    def get_data(self, key):
        return self.data[key]

    # 将cookie写入json文件
    def write_json(self, data):
        with open(r"../dataconfigure/cookie.json", 'w') as fp:
            fp.write(json.dumps(data))


