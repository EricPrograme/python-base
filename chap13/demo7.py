# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 16:59

"""

多态

"""


class Animal:
    def eat(self):
        print("动物吃东西...")


class Dog(Animal):
    def eat(self):
        print("狗吃肉...")


class Cat(Animal):
    def eat(self):
        print("猫吃鱼...")


class Person:
    def eat(self):
        print("人吃五谷杂粮...")


# 定义一个函数
def fun(obj):
    obj.eat()


fun(Dog())
fun(Cat())
fun(Animal())

print('-----------------------')

fun(Person())
