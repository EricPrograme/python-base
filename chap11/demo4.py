# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/25 16:36

"""

异常处理机制

1、 try ..except .. 结构

"""

try:
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))

    result = a / b
    print('输出的结果为：', result)
except ZeroDivisionError:
    print("除数不能为零")
except ValueError:
    print("请输入一个数字")
except BaseException as e:
    print(e)
print("程序结束")
