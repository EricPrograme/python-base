# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
列出指定目录的.py文件

E:\eric\python\chap15

"""

import os

path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith(".py"):
        print(filename)

