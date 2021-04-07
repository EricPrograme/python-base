#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: hmchen
@software: PyCharm
@file: demo_getattr.py
@time: 2021/3/19 
"""


class A(object):
    bar = 1


a = A()
print(getattr(a, 'bar'))

if __name__ == '__main__':
    pass
