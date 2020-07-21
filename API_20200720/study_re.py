# _*_coding:utf-8 _*_

# @Time:2020/7/7   23:10

# @Author: zlin

#@ File:study_re.py

#@Software:PyCharm

#@Desc: 解析正则表达式-->查找

import re
from API_20200720.common.config import config

data = '{"mobilephone":"#normal_user#", "pwd":"#normal_pwd#"}'

# # 原本字符，元字符
# # p = '#.*?#' # 从任意位置开始，找到一个就返回
 # m = re.search(p, data)
# print(m)
# print(m.group(0)) # 返回表达式和组里面的内容
# print(m.group(1)) # 返回指定组里面的内容
# g = m.group(1) # 拿到参数化的key
# v = config.get('data', g) # 根据key取到配置文件中的值
# print(v)
# # data_new = re.sub(p, v, data) # 查找替换
# data_new = re.sub(p, v, data, count=1) # 查找替换 count=1表示被替换的次数
# print(data_new)
# ms = re.findall(p, data) # 查找全部，返回列表
# print(ms)

# 如果要匹配多次，替换多次，用循环来解决
while re.search(p, data):
    print(data)
    m = re.search(p, data)
    g = m.group(1)  # 拿到参数化的key
    v = config.get('data', g)  # 根据key取到配置文件中的值
    print(v)
    data = re.sub(p, v, data, count=1)  # 查找替换 count=1表示被替换的次数
print(data)