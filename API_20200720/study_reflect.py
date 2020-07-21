# _*_coding:utf-8 _*_

# @Time:2020/7/19   19:44

# @Author: zlin

#@ File:study_reflect.py

#@Software:PyCharm

#@Desc: 类的反射：可以动态的查看、增加、删除、更改类或者实例的属性

class Penple:
    number_eye = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p = Penple('zlin', 24)
    print(Penple.number_eye)
    print(p.number_eye)
    print(p.name)

    # 操作类属性：判断、添加、获取  先判断属性有没有，有返回True
    print(hasattr(Penple, "number_eye"))
    print(hasattr(Penple, "number_leg"))
    setattr(Penple, "number_leg", 2)
    print(hasattr(Penple, "number_leg"))
    print(getattr(Penple, "number_leg"))

    # 操作实例属性：添加、获取、删除
    setattr(p, "dance", True)
    print(p.dance)
    print(getattr(p, "dance"))
    delattr(p, "dance")
    # print(getattr(p, "dance")) 因为已经删掉了，所以这里执行的时候回报错

    # 修改实力属性值
    setattr(p, "name", "zlinlyre")
    print(p.name)


