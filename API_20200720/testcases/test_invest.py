# _*_coding:utf-8 _*_

# @Time:2020/7/19   20:20

# @Author: zlin

#@ File:test_invest.py

#@Software:PyCharm

#@Desc: 投资接口
import unittest
from API_20200720.common.http_request import HttpRequest2
from API_20200720.common import do_execl
from API_20200720.common import contants
from API_20200720.common import context
from API_20200720.common.context import Context
from API_20200720.common import do_mysql
from ddt import ddt,data

@ddt #注意运行时要在测试类中执行，如果在测试方法中执行报错
class InvestTest(unittest.TestCase):
    execl = do_execl.DoExecl(contants.case_file, 'invest')
    cases = execl.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_invest(self, case):
        print("开始执行测试：", case.title)
        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected), actual_code)
            self.execl.write_result(case.case_id+1, resp.text, 'SUCCESS')

            # 判断加标成功之后，查询数据库，取到loan_id
            if resp.json()["msg"] == "加标成功":
                sql = 'select id from future.loan where memberid = 88538 order by id desc limit 1'
                loan_id = self.mysql.fetch_one(sql)[0]
                print("加标之后的标的id", loan_id)
                # 报存到类属性中
                setattr(Context, "loan_id", str(loan_id))

        except AssertionError as e:
            self.execl.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()