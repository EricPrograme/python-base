# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 15:17


"""
自定义计算器
被导包引用测试

"""


def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    # 只有当点击允许calc2时，才会执行运算
    print(add(10,20))



