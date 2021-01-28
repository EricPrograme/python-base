# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
with语句
上下文详解

"""


class MyContentMgr(object):
    def __enter__(self):
        print("enter方法被调用了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用了")

    def show(self):
        # 就算报错了，也会执行exit方法
        print("show 方法被调用了", 1/0)


# 使用with 相当于file =MyContentMgr()
with MyContentMgr() as file:
    file.show()
