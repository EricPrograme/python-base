#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: hmchen
@software: PyCharm
@file: demo_lambda.py
@time: 2021/3/11 
"""
from itertools import groupby

""" 匿名函数 """


# 无参数
lambda_a = lambda: 100
print('lambda_a()',lambda_a())

# 一个参数
lambda_b = lambda num: num * 10
print(lambda_b(5))

# 多个参数
lambda_c = lambda a, b, c, d: a + b + c + d
print(lambda_c(1, 2, 3, 4))

# 表达式分支
lambda_d = lambda x: x if x % 2 == 0 else x + 1
print(lambda_d(6))
print(lambda_d(7))


# lambda作为一个参数传递
def sub_func(a, b, func):
    print('a =', a)
    print('b =', b)
    print('a - b =', func(a, b))


sub_func(100, 1, lambda a, b: a - b)




member_list = [
    {"name": "风清扬", "age": 99, "power": 10000},
    {"name": "无崖子", "age": 89, "power": 9000},
    {"name": "王重阳", "age": 120, "power": 8000},
    {"name": "风清扬2", "age": 55, "power": 55},
    {"name": "王重阳2", "age": 1, "power": 8}
]
new_list = sorted(member_list,key=lambda dict_:dict_['age'])
# print('new_list',new_list)

for key1,value1 in groupby(member_list,key = lambda dict_:dict_['name']):
    print('key1',key1)
    # print('value1', value1)
    print('list(value1) :',list(value1))
    for item in value1:
        print
dict__ = {key1: [value2 for value2 in value1 ] for key1,value1 in groupby(member_list,key = lambda dict_:dict_['name'])}
# dict__ = {key1: list(value1) for key1,value1 in groupby(member_list,key = lambda dict_:dict_['name'])}
print('dict__',dict__)









salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}

def get(k):
    return salaries[k]

print(max(salaries,key=get)) #'alex'
print(max(salaries,key=lambda x:salaries[x]))

info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]

key=lambda dic: int(dic['salary'])

max(info, key=lambda dic: int(dic['salary']))
max([11, 22, 33, 44, 55])




version_dict = {'bds-server': '1.0.0-DEV', 'bms-server': '1.0.0-DEV'}
# for dict in version_dict.keys():
#     print(dict)

modify_module_list = [modify_module for modify_module in version_dict.keys()]
print(modify_module_list)



if __name__ == '__main__':
    pass
