# coding=utf-8
from data.get_data import GetData
from Base.RunMethod import RunMain
import json
import requests


class data_retrieve:
    def __init__(self, cookies):
        self.func_dict = {"del_zone": self.del_zone, "del_dep": self.del_dep, "del_device": self.del_device,
                          "del_emp": self.del_emp}
        self.run = RunMain()
        self.cookies = cookies

    def zone_data(self, data):
        """
        处理添加zone数据,格式化数据，使data中的zonenumber变为&K形势
        :param data: {'Data': [{'zoneNumber': 1, 'zoneName': 'just'}, ]}
        :return:['&K=1', ]
        """
        data = data["Data"]
        zone_list = []
        for i in data:
            zoneNum = i["zoneNumber"]
            s = '&K='+str(zoneNum)
            zone_list.append(s)
        return(''.join(zone_list))
        # print(type(''.join(zone_list)))

    def dep_emp_data(self, data, keyword1, keyword2=None):
        """
        处理department，employee数据，从数据中取zonenumber和deparmentcode/employeeID值
        :param data: {"Data": [{"zoneNumber": 1, "departmentCode": "1", "departmentName": "1"},]}
        :param keyword1:要获取的关键字，如 "departmentCode"
        :param keyword2:重新组合成dic中的元素名
        :return: [{'zoneNumber': 1, 'departmentCode': ['1',]},
        """
        dep_data = data["Data"]
        zone_list = []
        dep = []
        dep_list = []
        dic_list = []
        while len(dep_data):
            temp = dep_data[0]
            zone_list.append(dep_data[0]["zoneNumber"])
            dep.append(dep_data[0][keyword1])
            del dep_data[0]
            j = len(dep_data)
            while j:
                if dep_data[0]["zoneNumber"] == temp["zoneNumber"]:
                    dep.append(dep_data[0][keyword1])
                    del dep_data[0]
                j = j-1
            dep_list.append(dep)
            if keyword2:
                dic = {"zoneNumber": temp["zoneNumber"], "%s" % keyword2: dep}
            else:
                dic = {"zoneNumber": temp["zoneNumber"], "%s" % keyword1: dep}
            dic_list.append(dic)
            dep = []
        # print(zone_list, dep_list)
        return (dic_list)

    def dev_data(self, data):
        """
        从数据中取sn的值
        :param data:{"Data":[{"sn":"12345678", "zoneNumber":1, "departmentCode":"7", "alias":"test",
                            "masterDevice":"Yes", "facialDevice":"No"},]}
        :return:['12345678',]
        """
        data = data["Data"]
        dev_list = []
        for i in data:
            dev = i["sn"]
            dev_list.append(dev)
        dic = {'sn': dev_list}
        return dic

    def del_zone(self, data):
        url = "http://127.0.0.1:8081/iclock/data/company/?action=del"
        data = self.zone_data(data)
        res = requests.post(url=url, data=data, cookies=self.cookies)
        return res

    def del_dep(self, data):
        url = "http://127.0.0.1:8081/api/delete/departments/"
        data = self.dep_emp_data(data, "departmentCode")
        # print(data)
        for i in data:
            j = json.dumps(i)
            requests.post(url=url, data=j, cookies=self.cookies)

    def del_device(self, data):
        url = "http://127.0.0.1:8081/api/delete/devices/"
        data = self.dev_data(data)
        data = json.dumps(data)
        # print(data)
        # print(type(data))
        res = requests.post(url=url, data=data, cookies=self.cookies)
        return res

    def del_emp(self, data):
        url = "http://127.0.0.1:8081/api/delete/employees/"
        data = self.dep_emp_data(data, "ID", "empID")
        # print(data)
        for i in data:
            j = json.dumps(i)
            requests.post(url=url, data=j, cookies=self.cookies)

    def data_retrive(self, action, data):
        self.func_dict[action](data)

# zone_data = {"Data":[{"zoneNumber":1, "zoneName":"just"}, {"zoneNumber":2, "zoneName":"test"}, {"zoneNumber":3, "zoneName":"demo"}]}
# dep_data = {"Data": [{"zoneNumber": 1, "departmentCode": "1", "departmentName": "1"},
#                 {"zoneNumber": 1, "departmentCode": "2", "departmentName": "2"},
#                 {"zoneNumber": 2, "departmentCode": "1", "departmentName": "1"},
#                 {"zoneNumber": 2, "departmentCode": "2", "departmentName": "2"}]}
# emp_data = {"Data": [{"zoneNumber": 1, "ID": "000000003", "departmentCode": [1, 2, 3], "name":"test", "pin":"123",
#                      "idCard":"1234678", "privilege":0, "gender":"M"},
#                      {"zoneNumber": 1, "ID": "000000004", "departmentCode": [1, 2, 3], "name":"test", "pin":"123",
#                      "idCard":"1234678", "privilege":0, "gender":"M"},
#                      {"zoneNumber": 2, "ID": "000000006", "departmentCode": [1, 2], "name":"test", "pin":"123",
#                      "idCard":"1234678", "privilege":0, "gender":"M"}]}
# dev_data = {"Data":[{"sn":"12345678", "zoneNumber":1, "departmentCode":"7", "alias":"test","masterDevice":"Yes", "facialDevice":"No"},
#                   {"sn":"111111111", "zoneNumber":1, "departmentCode":"7", "alias":"test","masterDevice":"Yes", "facialDevice":"No"}]}
# # D = data_retrieve(dep_data)
# cookie = {
#     # 'Cookie': "sessionid=3b7b71fa0d88171b49b666376be1574a",
#     'sessionid':"10fac52a43f76b410a25a00c43fda325"
#     }
#
# D = data_retrieve(cookie)
# # D.del_zone(zone_data)
# # D.del_dep(dep_data)
# # D.del_emp(emp_data)
# D.data_retrive("del_zone", zone_data)
