# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/26 15:51

"""

封装
继承
多态

"""


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动')


car = Car("宝马X5")
car.start()
print(car.brand)



