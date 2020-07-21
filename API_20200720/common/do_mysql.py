# _*_coding:utf-8 _*_

# @Time:2020/6/29   20:33

# @Author: zlin

#@ File:do_mysql.py

#@Software:PyCharm

#@Desc:
import pymysql

class DoMysql:
    def __init__(self):
        host = "test.lemonban.com"  # 双引号
        user = "test"
        password = "test"
        port = 3306  # 没有引号
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        #  设置游标为字典类型的，否则为元祖
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) # 创建游标

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close() #关闭游标
        self.mysql.close() #关闭连接

if __name__ == '__main__':
    mysql = DoMysql()
    # mysql.connect() #可以在初始化的时候操作，所以这里可以把connect()--> __init__
    result = mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    mysql.close()
