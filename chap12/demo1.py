# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 11:31

"""

类 与对象
类属性，类方法，静态方法

"""

# Student 为类的名称，由一个或者多个单词组成，每个单词的首字母大写，其余小写


class Studen:
    # 直接写在类里的变量，称为类属性
    native_pace = '北京'
    def __init__(self, name, age):
        # self.name 称为实体属性，进行 一个赋值的操作，将局部变量的name的值赋给实体属性。
        self.name = name
        self.age = age

     # 实例方法
    def eat(self):
        print("吃饭")

    # 静态方法
    @staticmethod
    def method():
        print("我使用staticmethod进行修饰，所以我是静态方法。")

    # 类方法
    @classmethod
    def cm(cls):
        print("我是类方法，我使用了classmethod修饰。")


def drink():
    print("喝水")


# 创建Student类对象
print("------实例对象----------")
stu1 = Studen("张三", 20)
print(id(stu1))
print(type(stu1))
print(stu1)

# 对象名.方法
stu1.eat()
print(stu1.name)
print(stu1.age)

print("--------类的名称,类对象-----------")

# 类的名称
print(id(Studen))
print(type(Studen))
print(Studen)

# 类名.方法(类的对象) 实际上就是方法定义处的self
Studen.eat(stu1) # 与stu1.eat()的功能相同，都是调用Studen中的eat方法


print("--------------类属性的使用方式------------------------")
print(Studen.native_pace)

stu3 = Studen("张三", 20)
stu4 = Studen("李思", 30)
print(stu3.native_pace)
print(stu4.native_pace)

Studen.native_pace = "武汉"

print(stu3.native_pace)
print(stu4.native_pace)

# 类方法
Studen.cm()
print("---------------------------")
# 静态方法
Studen.method()
