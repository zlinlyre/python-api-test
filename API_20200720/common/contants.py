# _*_coding:utf-8 _*_

# @Time:2020/6/28   21:54

# @Author: zlin

#@ File:contants.py

#@Software:PyCharm

#@Desc:获取用例的绝对路径
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
# print(case_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
online_file = os.path.join(base_dir, 'config', 'online.conf')
test_file = os.path.join(base_dir, 'config', 'test.conf')

log_dir = os.path.join(base_dir, 'log')

case_dir = os.path.join(base_dir, 'testcases')

report_dir = os.path.join(base_dir, 'reports')