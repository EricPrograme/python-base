# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""

os文件操作

os.path函数的使用
"""

import os.path

# 返回文件的绝对路径
print(os.path.abspath('demo1.py'))

# 判断文件是否存在
print(os.path.exists("demo1.py"),os.path.exists('demo.py'))

# 路径拼接操作
print(os.path.join("E:\eric\python","demo1"))

# 把文件与路径拆分
print(os.path.split('E:\\eric\\python\\chap15\\demo1.py'))

# 把文件名与后缀名进行拆分
print(os.path.splitext("demo1.py"))

# 从目录中提取文件名
print(os.path.basename("E:\eric\python\chap15\demo1.py"))

# 从目录中提取目录
print(os.path.dirname("E:\eric\python\chap15\demo1.py"))

# 判断是否是目录
print(os.path.isdir("E:\eric\python\chap15\demo1.py"))