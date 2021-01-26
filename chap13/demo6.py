# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 16:49


"""
Object 类

"""


class Student():
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "我的名字是：{0},我今年{1}岁了".format(self.name, self.age)


stu = Student("张三", 22)
print(dir(stu))
print(stu)
print(type(stu))