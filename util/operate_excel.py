# coding:utf-8
import xlrd
from xlutils.copy import copy


class OperateExcel:

    def __init__(self, path=None, sheetID=None):
        if path:
            self.path = path
            self.data = xlrd.open_workbook(self.path)
            self.table = self.data.sheets()[sheetID]
        else:
            self.path = r"../dataconfigure/wdms.xls"
            self.data = xlrd.open_workbook(self.path)
            self.table = self.data.sheets()[0]
        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    # 获取某单元格值
    def get_cell_value(self, row, col):
        return self.table.cell_value(row, col)

    # 写数据
    def write_data(self, row, col, value):
        # write_data = xlrd.open_workbook(self.path)
        write_data = copy(self.data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.path)

    # 获取表格所有内容，并返回dict
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于 1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应 values 值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                    r.append(s)
                    j += 1
                return r

    # 获取表格所有内容，并返回list
    def list_data(self):
        r = []
        for row in range(1, self.rowNum):
            r.append(self.table.row_values(row))
        return r

    # 根据case_id找到对应行的的内容
    def get_row_data(self, case_id, col=None):
        row_id = self.get_row_num(case_id, col)
        row_data = self.get_row_value(row_id)
        return row_data

    # 根据case_id找到对应的行
    def get_row_num(self, case_id, col=None):
        num = 0
        cols_data = self.get_col_value(col)
        # print(case_id, type(case_id))
        # print(cols_data,type(cols_data))
        for col_data in cols_data:
            if case_id in col_data:
                return num
            else:
                num = num+1

    # 获取某行的值
    def get_row_value(self, row):
        return self.table.row_values(row)

    # 获取某列的值
    def get_col_value(self, col=None):
        if col:
            return self.table.col_values(col)
        else:
            return self.table.col_values(0)


# if __name__ == "__main__":
#     # filepath = r'C:\Users\Administrator\Desktop\wdms.xls'
#     data = OperateExcel()
#     a = data.get_col_value(2)
#     print(a)
#     # for i in range(6):
#     #     # filepath = r'C:\Users\Administrator\Desktop\wdms.xls'
#     #     # data = OperateExcel(filepath, 0)
#     #     if i % 2 == 0:
#     #         data.write_data(i, 15, 'hello')
#     #     else:
#     #         data.write_data(i, 15, 'hi')

