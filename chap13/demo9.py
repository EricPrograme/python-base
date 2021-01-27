# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 9:42


"""

Python的特殊方法

"""

a = 20
b = 100
# 两个整数类型的对象的相加操作
c = a + b

d = a.__add__(b)
print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    # 自定义
    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("JACK")
stu2 = Student("李四")

# 实现了两个对象的加法运算，因为在Student类中，编写了__add__()特殊方法
s = stu1+stu2

s1= stu1.__add__(stu2)
print(s)
print(s1)

print("------------------len--------------------------------")

lst = [11, 22, 33, 44]
# len()是内容函数len
print(len(lst))
print(lst.__len__())
print(len(stu1))

