# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 16:07

"""

继承

"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("姓名 :{0}, 年龄：{1}".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self,name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


stu = Student("张三", 20, '9887')
teacher = Teacher("李思", 60, 30)

stu.info()
teacher.info()

