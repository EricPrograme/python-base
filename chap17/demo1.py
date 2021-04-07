#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: hmchen
# DATE  : 2021/3/9 20:58

"""
实操案例

任务一、 想文件输出‘奋斗成就更好的你’

任务二、输出北京天气预报

任务三、机票购买界面

任务四、北京地铁1号线运行图


"""


# 任务一：

""" 1、使用print方式进行输出 （输出的是目的文件） """
import os

print(os.getcwd())
txt_file = os.getcwd()+'/test.txt'
fp = open(txt_file, 'w', encoding='utf-8')
print('奋斗成就更好的你', file=fp)
fp.close()


"""第二种方式，使用文件读写操作"""

with open(txt_file,'w') as file:
    file.write('奋斗成就更好的你2')

# 任务二：

