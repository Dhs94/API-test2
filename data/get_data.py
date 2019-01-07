# coding:utf-8
from util.operate_json import OperateJson
from util.operate_excel import OperateExcel
from data.data_configure import *
from util.operate_header import OperateHeader
from Base.RunMethod import RunMain
from util.connect_db import OperateMysql
import json


class GetData:

    def __init__(self):
        self.excel = OperateExcel()

    # 获取row
    def get_case_lines(self):
        lines = self.excel.rowNum
        return lines

    # 获取是否执行
    def get_is_run(self, row):
        col = get_run()
        run = self.excel.get_cell_value(row, col)
        if run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取是否有header
    # def get_case_header(self, row):
    #     header_col = get_header()
    #     header = self.excel.get_cell_value(row, header_col)
    #     return header

    # 获取请求方式
    def get_case_method(self, row):
        col = get_request_way()
        method = self.excel.get_cell_value(row, col)
        return method

    # 获取url
    def get_case_url(self, row):
        col = get_url()
        url = self.excel.get_cell_value(row, col)
        return url

    # 获预期结果的json关键字
    def get_expect_key(self, row):
        col = get_expect()
        expect = self.excel.get_cell_value(row, col)
        return expect

    # 获取预期结果
    def get_case_expect(self, row):
        expect4json = self.get_expect_key(row)
        expect = OperateJson(r"../dataconfigure/expect.json").get_data(expect4json)
        return expect

    # 从数据库总获取数据
    def get_case_expect_from_mysql(self, row):
        op_mysql = OperateMysql()
        key4sql = self.get_expect_key(row)
        expect = op_mysql.search_all(sql=key4sql)
        return expect

    # 获取实际结果
    def get_case_result(self, row):
        col = get_result()
        result = self.excel.get_cell_value(row, col)
        return result

    # 获取data的json关键字
    def get_data_key(self, row):
        col = get_data()
        data = self.excel.get_cell_value(row, col)
        return data

    # 获取请求数据
    def get_case_data(self, row):
        data4json = self.get_data_key(row)
        if data4json == '':
            request_data = None
        else:
            request_data = OperateJson().get_data(data4json)
        return request_data


    # 写数据
    def write_result(self, row, value):
        col = get_result()
        self.excel.write_data(row, col, value)

    # 获取依赖id
    def get_depend_case_id(self, row):
        col = get_case_depend()
        case_id = self.excel.get_cell_value(row, col)
        if case_id == "":
            return None
        else:
            return case_id

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = get_data_depend()
        depend_key = self.excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 获取依赖数字所属字段
    def get_depend_field(self, row):
        col = get_field_depend()
        depend_field = self.excel.get_cell_value(row, col)
        if depend_field == "":
            return None
        else:
            return depend_field

    # 获取header
    def get_case_header(self, row, url, request_data):
        """
        :param row:
        :param url:
        :param request_data:
        :return: 若header为write，则写入cookie，返回None，若为yes则获取cookie，若为no则返回none
        """
        header_col = get_header()
        header = self.excel.get_cell_value(row, header_col)
        if header == "write":
            op_header = OperateHeader()
            op_header.write_cookies(url=url, data=request_data)
            return None
        elif header == "yes":
            op_json = OperateJson(r"../dataconfigure/cookie.json")
            value = op_json.get_data("sessionid")
            cookie = {
                "sessionid": value
            }
            return cookie
        else:
            return None

    def get_all_data(self, row):
        data = {}
        data["is_run"] = self.get_is_run(row)
        if data["is_run"]:
            data["url"] = self.get_case_url(row)
            data["method"] = self.get_case_method(row)
            data["expect"] = self.get_case_expect(row)
            data["depend_case_id"] = self.get_depend_case_id(row)
            data["request_data"] = self.get_case_data(row)
            data["cookie"] = self.get_case_header(row, url=data["url"], request_data=data["request_data"])
        return data


if __name__ == '__main__':
    res = RunMain()
    data = GetData()
    excel = OperateExcel()
    expect = data.get_case_expect_from_mysql(3)
    print(expect)
    print(type(expect))












