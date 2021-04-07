# Author: hmchen
# DATE  : 2021/3/14 11:03


class CLanguage :
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    def __init__(self,name,add):
        #下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name,"网址为：",add)
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)
# 将该CLanguage对象赋给clanguage变量
clanguage = CLanguage("C语言中文网","http://c.biancheng.net")


# 给类对象动态添加方法
def info(self):
    print('info 函数', self)

clanguage.foo = info
clanguage.foo(clanguage)


clanguage.bar = lambda self: print('lambda表达式', self)
clanguage.bar(clanguage)


# 有没有不用手动给 self 传值的方法呢？通过借助 types 模块下的 MethodType 可以实现
def info(self, content):
    print("C语言中文网地址为：%s" % content)
# 导入MethodType
from types import MethodType
clanguage.info = MethodType(info, clanguage)
# 第一个参数已经绑定了，无需传入
clanguage.info("http://c.biancheng.net")