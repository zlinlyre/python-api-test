# _*_coding:utf-8 _*_

# @Time:2020/6/23   23:23

# @Author: zlin

#@ File:http_request.py

#@Software:PyCharm

#@Desc: 20200618内容封装
        # (1)cookies
        # (2)session

import requests
from API_20200720.common.config import config
from API_20200720.common import logger

logger = logger.get_logger(__name__)

class HttpRequest:
    def request(self, method, url, data, json=None, cookies=None):
        method = method.upper() #method强制转大写

        if type(data) == str:
            data = eval(data)

        if method == 'GET':
            resp = requests.get(url, params=data, cookies=cookies)
        elif method == 'POST':
            if json:
                resp = requests.post(url, json=data, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            print("UN-support method")
        print("请求url:", resp.url)
        print("请求response:", resp.text)
        return resp

class HttpRequest2:
    def __init__(self):
        self.session = requests.sessions.session() #打开一个session
    def request(self, method, url, data, json=None):
        method = method.upper() #method强制转大写

        #str转成字典
        if type(data) == str:
            data = eval(data)
        # 拼接请求的URL
        url = config.get('api', 'pre_url')+url
        logger.debug("请求url:{0}".format(url))
        logger.debug("请求data:{0}".format(data))

        if method == 'GET':
            resp = self.session.request(method, url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method, url, json=data)
            else:
                resp = self.session.request(method, url, data=data)
        else:
            logger.error("UN-support method")
        logger.debug("请求response:{0}".format(resp.text))
        return resp
    def close(self): # 用完记得关闭，很关键！！！
        self.session.close()


# if __name__ == '__main__':
#     http_request = HttpRequest()
#     #调用登录
#     params = {"mobilephone": "18829348425", "pwd": "111111"}
#     resp = http_request.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)
#     #调用充值
#     params = {"mobilephone": "18829348425", "amount": "1000"}
#     resp = http_request.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params, cookies=resp.cookies)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)

if __name__ == '__main__':
    http_request2 = HttpRequest2()
    #调用登录
    params = {"mobilephone": "18829348425", "pwd": "111111"}
    resp2 = http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)
    #调用充值
    params = {"mobilephone": "18829348425", "amount": "1000"}
    resp2 = http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)
    http_request2.close()#如果没有关闭，少量请求没问题，多次请求会报错