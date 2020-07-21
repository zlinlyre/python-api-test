# _*_coding:utf-8 _*_

# @Time:2020/6/29   20:12

# @Author: zlin

#@ File:study_pymysql.py

#@Software:PyCharm

#@Desc:连接数据库
import pymysql

# 建立连接-->新建查询界面--> 编写SQL--> 执行SQL--> 查看结果-->关闭查询--> 关闭数据库连接
host = "test.lemonban.com" #双引号
user = "test"
password = "test"
port = 3306 # 没有引号
mysql = pymysql.connect(host=host, user=user, password=password, port=port)
cursor = mysql.cursor()
sql = 'select max(mobilephone) from future.member'
# sql = 'select * from future.loan limit 10'
cursor.execute(sql)
result = cursor.fetchone() #查询结果集中最近的一条进行返回
# result = cursor.fetchall() #获取全部结果集
print(type(result), result[0])
cursor.close()
mysql.close()