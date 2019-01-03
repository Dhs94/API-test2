# coding: utf-8
import json
import operator


class CommonUtil:
    def is_contain(self, str1, str2):
        """
        判断str1是否在str2中
        :param str1: 预期结果
        :param str2:实际结果
        :return:如果str1在str2中返回True,反之返回False
        """
        # if type(str1) == dict:
        #     str1 = json.dumps(str1)

        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_to(self, dict1, dict2):
        """
        判断dict1与dict2是否相等
        :param dict1: 预期结果
        :param dict2: 实际结果
        :return: 相等返回true，不等返回false
        """
        if isinstance(dict1, str):
            dict1 = json.loads(dict1)
        if isinstance(dict2, str):
            dict2 = json.loads(dict2)
        return operator.eq(dict1, dict2)


