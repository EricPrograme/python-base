# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 9:42


"""

Python的特殊方法

"""


class Person:
    def __init__(self, name, age):
        print("__init_被调用了，self的id值为{0}".format(id(self)))
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__被调用了，cls的id值为{0}".format(id(cls)))
        obj = super().__new__(cls)
        print("创建对象的id为{0}:".format(id(obj)))
        return  obj


print("object 这个类对象的id为:{0}".format(id(object)))
print("person 这个类对象的id为:{0}".format(id(Person)))

# 创建Person类的实例对象
p1 = Person("张三", 20)
print("p1 这个实例对象的id 值为:{0}".format(id(p1)))


