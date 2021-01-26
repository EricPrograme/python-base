# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 11:31

"""

 类和对象
 实例对象动态绑定属性和方法

"""


class Studen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "在吃饭")


# 一个Student类可以创建N多个Student类的实例对象，每个实例对象的属性值不同。
stu1 = Studen("张三", 20)
stu2 = Studen("李四", 30)
print(id(stu1))
print(id(stu2))

# 动态绑定,为stu2动态绑定性别属性
stu2.gender = '女'

print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print("--------------------------")
stu1.eat()
stu2.eat()


def show():
    print("定义在类之外的，称为函数")


stu1.show = show
stu1.show()

# stu2.show() 报错，因为stu2没有动态绑定show方法




