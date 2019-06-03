# coding=utf-8
from Base.RunMethod import RunMain


class data_retrives:

    def __init__(self, data):
        self.data = data
        self.run_request = RunMain()
        self.func = {"del_zone": self.del_zone, "del_dep": self.del_dep, "del_dev": self.del_dep, "del_emp": self.del_emp}

    def del_zone(self):
        print("del zone")

    def del_dep(self):
        print("del dep")

    def del_dev(self):
        print("del dev")

    def del_emp(self):
        print("del emp")

    def delete(self, x):
        self.func.get(x)()

