# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/25 16:36

"""

异常处理机制

2、 try ..except..else  结构

"""

try:
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    result = a / b
except BaseException as e:
    print('出错了！', e)
else:
    print('输出的结果为：', result)

print("程序结束")
