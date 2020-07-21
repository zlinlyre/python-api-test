# _*_coding:utf-8 _*_

# @Time:2020/7/20   11:05

# @Author: zlin

#@ File:logger.py

#@Software:PyCharm

#@Desc: 日志模块: logger不仅可以输出控制台，还可以输出文件
#                 print输出控制台

import logging
from API_20200720.common import contants

# 设置logger对象-name
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    # 定义日志格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt=fmt)

    console_handle = logging.StreamHandler() # 控制台
    # 把日志级别放到配置文件--优化
    console_handle.setLevel('DEBUG')
    console_handle.setFormatter(formatter)

    # 把日志级别放到配置文件--优化
    file_handle = logging.FileHandler(contants.log_dir+'/case.log', encoding="utf-8")
    file_handle.setLevel('INFO')
    file_handle.setFormatter(formatter)

    logger.addHandler(console_handle)
    logger.addHandler(file_handle)
    return logger

logger = get_logger('case')
logger.info('测试开始')
logger.error('测试报错')
logger.debug('测试数据')
logger.info('测试结束')
