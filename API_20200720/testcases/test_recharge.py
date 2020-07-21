# _*_coding:utf-8 _*_

# @Time:2020/6/28   23:12

# @Author: zlin

#@ File:test_recharge.py

#@Software:PyCharm

#@Desc:充值接口
# 类方法和实例方法的区别

import unittest
from API_20200720.common.http_request import HttpRequest2
from API_20200720.common import do_execl
from API_20200720.common import contants
from API_20200720.common.do_mysql import DoMysql
from ddt import ddt,data

@ddt #注意运行时要在测试类中执行，如果在测试方法中执行报错
class LoginTest(unittest.TestCase):
    execl = do_execl.DoExecl(contants.case_file, 'recharge')
    cases = execl.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_login(self, case):
        print(case.title)
        # 请求之前，判断是否要执行SQL
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetch_one(sql)
            # print(member['LeaveAmount'])
            before = member['LeaveAmount']

        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected), actual_code)
            self.execl.write_result(case.case_id+1, resp.text, 'SUCCESS')
            # 成功之后判断是否执行sql
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                # print(member['LeaveAmount'])
                after = member['LeaveAmount']

                recharge_amount = int(eval(case.data)['amount']) # 充值金额
                self.assertEqual(before+recharge_amount, after)
        except AssertionError as e:
            self.execl.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
