# _*_coding:utf-8 _*_

# @Time:2020/6/29   20:45

# @Author: zlin

#@ File:test_register.py

#@Software:PyCharm

#@Desc:
import unittest
from API_20200720.common.http_request import HttpRequest2
from API_20200720.common import do_execl
from API_20200720.common import contants
from ddt import ddt,data
from API_20200720.common import do_mysql

@ddt #注意运行时要在测试类中执行，如果在测试方法中执行报错
class RegisterTest(unittest.TestCase):
    execl = do_execl.DoExecl(contants.case_file, 'register')
    cases = execl.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_register(self, case):
        if case.data.find('register_mobile') > -1: # 判断参数化标识
            sql = 'select max(mobilephone) from future.member'
            max_phone = self.mysql.fetch_one(sql)[0] #查询最大的手机号码
            max_phone = int(max_phone) + 1
            # replace替换之后重新赋值给一个新的字符串
            case.data = case.data.replace('register_mobile', str(max_phone)) #用最大手机号码替换参数值
            print(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.execl.write_result(case.case_id+1, resp.text, 'SUCCESS')
        except AssertionError as e:
            self.execl.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
