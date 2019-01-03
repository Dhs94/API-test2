# coding:utf-8
import sys
sys.path.append("D:\\PycharmProjects\\WDMS")
from data.get_data import GetData
from Base.RunMethod import RunMain
from util.common_util import CommonUtil
from util.depend_data import DependData
from util.send_mail import SendMail


class RunTest:
    def __init__(self):
        self.data = GetData()
        self.run_method = RunMain()
        self.common = CommonUtil()
        self.sendMail = SendMail()

    # 程序执行的接口
    def go_on_run(self):
        pass_count = []
        fail_count = []
        count = self.data.get_case_lines()
        for i in range(1, count):
            # 每一次循环都写了数据，所以需要在for循环里对data进行实例化，若在for外进行实例化则只保存最后一次循环写的数据
            get_data = GetData()
            data = get_data.get_all_data(i)
            if data["is_run"]:
                # 是否有依赖case
                depend_data = DependData(data["depend_case_id"])
                data["request_data"] = depend_data.is_run_depend_case(i, data["request_data"], "Data", 0)
                if data["cookie"]:
                    res = self.run_method.run_request(data["method"], data["url"], data["request_data"], data["cookie"])
                else:
                    res = self.run_method.run_request(data["method"], data["url"], data["request_data"])
                print(data["expect"])
                print(res)
                # 判断预期结果与运行结果是否相符
                if self.common.is_equal_to(dict1=data["expect"], dict2=res):
                    get_data.write_result(i, "Pass")
                    pass_count.append(i)
                    print("--------Pass--------")
                else:
                    get_data.write_result(i, res)
                    fail_count.append(i)
                    print("-------Failed--------")
        # self.sendMail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run_test = RunTest()
    run_test.go_on_run()

# # 封装前
# class RunTest:
#     def __init__(self):
#         self.data = GetData()
#         self.run_method = RunMain()
#         self.common = CommonUtil()
#         self.sendMail = SendMail()
#
#     # 程序执行的接口
#     def go_on_run(self):
#         pass_count = []
#         fail_count = []
#         count = self.data.get_case_liens()
#         for i in range(1, count):
#             # 每一次循环都写了数据，所以需要在for循环里对data进行实例化，
#             # 若在for外进行实例化则只保存最后一次循环写的数据
#             data = GetData()
#             is_run = self.data.get_is_run(i)
#             if is_run:
#                 url = self.data.get_case_url(i)
#                 method = self.data.get_case_method(i)
#                 expect = self.data.get_case_expect(i)
#                 depend_case_id = self.data.get_depend_case_id(i)
#                 request_data = self.data.get_case_data(i)
#                 cookies = self.data.get_case_header(i, url, request_data)
#                 # 是否有依赖case
#                 if depend_case_id:
#                     depend_data = DependData(depend_case_id)
#                     depend_response_data = depend_data.get_data4key(i)
#                     depend_field = self.data.get_depend_field(i)
#                     # 根据request_data格式
#                     request_data["Data"][0][depend_field] = depend_response_data
#                 if cookies:
#                     res = self.run_method.run_request(method, url, request_data, cookies)
#                 else:
#                     res = self.run_method.run_request(method, url, request_data)
#                 print(res)
#                 # 判断预期结果与运行结果是否相符
#                 if self.common.is_equal_to(dict1=expect, dict2=res):
#                     data.write_result(i, "Pass")
#                     pass_count.append(i)
#                     print("--------Pass--------")
#                 else:
#                     data.write_result(i, res)
#                     fail_count.append(i)
#                     print("-------Failed--------")
#         # self.sendMail.send_main(pass_count, fail_count)
#
#
# if __name__ == '__main__':
#     run_test = RunTest()
#     run_test.go_on_run()

