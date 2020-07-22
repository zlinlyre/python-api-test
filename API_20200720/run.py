# _*_coding:utf-8 _*_

# @Time:2020/7/20   12:46

# @Author: zlin

#@ File:run.py.py

#@Software:PyCharm

#@Desc: 收集测试用例-放到测试套件中-在run中执行

import sys
sys.path.append('./') # progject根路径
print(sys.path)
import unittest
from API_20200720.testcases import test_login
from API_20200720.common import HTMLTestRunnerNew
from API_20200720.common import contants

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromModule(test_login))

# discover = unittest.defaultTestLoader.discover(contants.case_file, "test_*.py")

with open(contants.report_dir+'/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON15 API TEST REPORT",
                                              description="前程贷API")
    runner.run(suite)
    # runner.run(discover)

