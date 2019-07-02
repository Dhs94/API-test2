# coding:utf-8
from Base.RunMethod import RunMain
from util.operate_excel import OperateExcel
from data.get_data import GetData
from jsonpath_rw import parse, jsonpath
import json

class DependData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.excel = OperateExcel()
        self.data = GetData()
        self.run = RunMain()

    # 通过case_id获取对应的整行数据
    def get_case_line_data(self):
        row_data = self.excel.get_row_num(self.case_id)
        return row_data

    # 执行依赖测试，获取结果
    def run_depend(self):
        row_num = self.excel.get_row_num(self.case_id)
        request_data = self.data.get_case_data(row_num)
        url = self.data.get_case_url(row_num)
        header = self.data.get_case_header(row=row_num, url=url, request_data=request_data)
        request_method = self.data.get_case_method(row_num)
        response_data = self.run.run_request(method=request_method, url=url, data=request_data, cookies=header)
        # 将str转换为dict
        response_data = json.loads(response_data)
        return response_data

    # 根据依赖的key获取以来测试结果的返回值
    def get_data4key(self, row):
        depend_key = self.data.get_depend_key(row)
        # print(depend_key)
        response_data = self.run_depend()
        # print(response_data)
        # 在response_data中返回格式{'code':200,'data':[{'zoneName':1,'zoneNumber':1},{}]},depend_key传入data[0].zoneName,json_exe=data.[0].zoneName
        if depend_key:
            json_exe = parse(depend_key)
            # 在response_data中寻找dependkey
            madle = json_exe.find(response_data)
            # [math.value for math in madle]返回值为list[1]
            # print([math.value for math in madle])
            return [math.value for math in madle][0]

    # 判断是否执行依赖case
    def is_run_depend_case(self, row, request_data, request_data_key=None, request_data_num=None):
        if self.case_id:
            depend_response_data = self.get_data4key(row)
            depend_filed = self.data.get_depend_field(row)
            # 格式根据数据来写 如 {"data":[{"a":1,"b":2},{"a":3,"b":4}]}
            if depend_response_data and depend_filed:
                request_data[request_data_key][request_data_num][depend_filed] = depend_response_data
                return request_data[request_data_key][request_data_num][depend_filed]
            else:
                return request_data
        else:
            return request_data
# get_data = GetData()
# data = get_data.get_all_data(33)
# depend_data = DependData(data["depend_case_id"])
# data["request_data"] = depend_data.is_run_depend_case(33, data["request_data"], "Data", 0)












