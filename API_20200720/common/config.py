# _*_coding:utf-8 _*_

# @Time:2020/6/28   23:32

# @Author: zlin

#@ File:config.py

#@Software:PyCharm

#@Desc:配置文件的切换

import configparser
from API_20200720.common import contants

class ReadConfig:
     def __init__(self):
         self.config = configparser.ConfigParser()
         self.config.read(contants.global_file)
         switch = self.config.getboolean('switch', 'on')
         if switch:
             self.config.read(contants.online_file, encoding='utf-8')
         else:
             self.config.read(contants.test_file, encoding='utf-8')

     def get(self, section, option):
         return self.config.get(section, option)

config = ReadConfig()
# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api', 'pre_url'))