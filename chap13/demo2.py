# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 15:55

"""

封装

"""


class Student:
    def __init__(self, name, age):
        self.name = name
        # 年龄不希望在类的外部被使用，所以加了两个__ ，__ 类似与java 中的private 私有
        self.__age = age

    def show(self):
        print(self.name, self.__age)


# 在类的外部使用name 和age
stu = Student("张三", 22)
print(stu.name)
# print(stu.__age) 不能访问
print(dir(stu))
# 在类的外部可以通过_Student__age 进行访问
print(stu._Student__age)
