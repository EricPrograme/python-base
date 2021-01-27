# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 14:58


"""
模块

一个模块包含有 N多个函数，N多个类（类属性，类方法，静态方法,实例属性），N多个语句
"""


def fun():
    pass


def fun2():
    pass


class Student:
    native_place = '武汉'

    def __init__(self, name):
        self.name = name

    def eat(self, name):
        self.name = name
        pass


    classmethod
    def cm(self):
        pass

    staticmethod
    def sm(self):
        pass


a = 1
b = 2
print(a+b)


