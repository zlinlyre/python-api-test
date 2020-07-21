# _*_coding:utf-8 _*_

# @Time:2020/6/28   21:48

# @Author: zlin

#@ File:test_login.py

#@Software:PyCharm

#@Desc: 登录接口unittest+ddt --> login
import unittest
from API_20200720.common.http_request import HttpRequest2
from API_20200720.common import do_execl
from API_20200720.common import contants
from API_20200720.common import logger
from ddt import ddt,data

logger = logger.get_logger(__name__)

@ddt #注意运行时要在测试类中执行，如果在测试方法中执行报错
class LoginTest(unittest.TestCase):
    execl = do_execl.DoExecl(contants.case_file, 'login')
    cases = execl.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_login(self, case):
        logger.info("开始测试：{0}".format(case.title))
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.execl.write_result(case.case_id+1, resp.text, 'SUCCESS')
        except AssertionError as e:
            self.execl.write_result(case.case_id + 1, resp.text, 'FAIL')
            logger.error("测试报错：{0}".format(e))
            raise e
        logger.info("结束测试：{0}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info("测试后置处理")
        cls.http_request.close()
