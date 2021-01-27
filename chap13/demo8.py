# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 17:08


"""

Python的特殊属性


"""

# print(dir(object))


class A:
    pass


class B:
    pass


class C(B, A):
    def __init__(self, name ,age):
        self.name = name
        self.age = age


class D(A):
    pass


x = C("张三", 22)
# 实例对象的属性字典
print(x.__dict__)
print(C.__dict__)

print("--------------------------------------")
# 输出了对象所属类型
print("输出了对象所属类型：", x.__class__)

# C类的父类类型的元素
print("C类的父类类型的元素：", C.__bases__)
print("类的基类,继承最近的：", C.__base__)

# 类的层次结构
print("类的层次结构", C.__mro__)
# 子类的列表
print("子类的列表", A.__subclasses__())