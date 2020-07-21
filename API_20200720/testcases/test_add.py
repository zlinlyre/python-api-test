# _*_coding:utf-8 _*_

# @Time:2020/7/7   22:13

# @Author: zlin

#@ File:test_add.py

#@Software:PyCharm

#@Desc:加标接口

import unittest
from API_20200720.common.http_request import HttpRequest2
from API_20200720.common import do_execl
from API_20200720.common import contants
from API_20200720.common.config import config
from API_20200720.common import context
from ddt import ddt,data

@ddt #注意运行时要在测试类中执行，如果在测试方法中执行报错
class AddTest(unittest.TestCase):
    execl = do_execl.DoExecl(contants.case_file, 'add')
    cases = execl.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_add(self, case):

        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)

        # case.data = eval(case.data) # 变成字典
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #     case.data['mobilephone'] = config.get('data', 'normal_user')  # 拿到配置文件中的值
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
        #     case.data['pwd'] = config.get('data', 'normal_pwd')
        # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
        #     case.data['memberId'] = config.get('data', 'loan_member_id')

        # print(case.title)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected), actual_code)
            self.execl.write_result(case.case_id+1, resp.text, 'SUCCESS')
        except AssertionError as e:
            self.execl.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()