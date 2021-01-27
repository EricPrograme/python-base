# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 9:42


"""

1.变量的赋值
2.类的浅拷贝
3,类的深拷贝

"""
import copy


class CPU:
    pass


class DISK:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值

cpu1 = CPU()
cpu2 = cpu1

print(cpu1, id(cpu1))
print(cpu2, id(cpu2))


# 类的浅拷贝

print("--------------类的浅拷贝------------")
disk = DISK()
computer1 = Computer(cpu1, disk)


# 浅拷贝操作
computer2 = copy.copy(computer1)

print("实例化:", computer1, computer1.cpu, computer1.disk)
print("浅拷贝:", computer2, computer2.cpu, computer2.disk)

print("--------------类的深拷贝------------")
# 深拷贝
computer3 = copy.deepcopy(computer1)
print("实例化:", computer1, computer1.cpu, computer1.disk)
print("深拷贝:", computer3, computer3.cpu, computer3.disk)
