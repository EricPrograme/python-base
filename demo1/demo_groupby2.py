#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: hmchen
@software: PyCharm
@file: demo_groupby2.py
@time: 2021/3/22 
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': list('aabba'),
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})

for i in df.groupby("key1"):
    print('i=', i)

print("-------------------------------")
for i in df.groupby(['key1', 'key2']):
    print(i)

print("-------------------------------")
people = pd.DataFrame(
    np.random.randint(low=0, high=6, size=(5, 5)),
    columns=['香蕉', '苹果', '橘子', '眼影', '眼线'],
    index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis']
)

mapping = {'香蕉': '水果', '苹果': '水果', '橘子': '水果', '眼影': '化妆品', '眼线': '化妆品'}
data = people.groupby(mapping, axis=1).mean()
print(data)

mapping2 = pd.Series(mapping)
data2 = people.groupby(mapping2, axis=1).mean()
print(data2)
