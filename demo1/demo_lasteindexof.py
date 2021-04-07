#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: hmchen
@software: PyCharm
@file: demo_lasteindexof.py
@time: 2021/3/23 
"""

pom_path = r'E:/eric/auto/manage/gitlab/ntrm/1.1.0-CMO-SNAPSHOT/pub-portal/pom.xml'

str = pom_path.index('/')
print(str)
str2 = pom_path[pom_path.rfind("/") + 1:pom_path.rfind("/")]
print('str2:', str2)

start = pom_path.rindex("/")
end = pom_path[:start].rindex("/")
print('start', start)

print(pom_path[end + 1:start])

if __name__ == '__main__':
    pass
