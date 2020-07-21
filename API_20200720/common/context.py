# _*_coding:utf-8 _*_

# @Time:2020/7/7   23:39

# @Author: zlin

#@ File:context.py

#@Software:PyCharm

#@Desc:
import re
import configparser
from API_20200720.common.config import config

class Context:
    loan_id = None


def replace(data):
    p = '#(.*?)#'  # 从任意位置开始，找到全部就返回
    while re.search(p, data):
        m = re.search(p, data)
        g = m.group(1)  # 拿到参数化的key
        try:
            v = config.get('data', g)  # 根据key取到配置文件中的值
        # 如果配置文件中没有，去Context中取
        except configparser.NoOptionError as e:
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                print("找不到参数化的值！！！")
                raise e

        # print(v)
        data = re.sub(p, v, data, count=1)  # 查找替换 count=1表示被替换的次数
    return data