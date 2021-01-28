# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
with语句

"""

# 使用with 不用手动关闭
with open('a.txt', 'r', encoding='utf-8') as file:
    print(file.read())