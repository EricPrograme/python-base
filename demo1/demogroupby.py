#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: hmchen
@software: PyCharm
@file: demogroupby.py
@time: 2021/3/11 
"""

import pandas as pd
import json
from itertools import groupby

j = json.loads('[{"id":1,"name":"a"},'
               '{"id":1,"name":"b"},'
               '{"id":2,"age":32},'
               '{"id":1,"age":32},'
               '{"id":2,"name":"22"}]')
d = {}

# for key, value in groupby(j):
#     print('key :', key)
#     print('value :', value)
# lambda x: x

# def biz(a):
#     v = d[a['id']]
#     for k,v in a.iteriters():
#         if hasattr(v,k):
#             if isinstance(v,unicode):
#                 v[k] = v
#             else:
#                 v[k] = v if v> v[k] else v[k]
#         else:
#             v[k] = v


list2 = [{'module': 'bms-server', 'versiontag': 'bms-internal-api.version'},
         {'module': 'bms-server', 'versiontag': 'bms-external-api.version'},
         {'module': 'bms-server', 'versiontag': 'bms-external-impl.version'},
         {'module': 'bms-server', 'versiontag': 'bms.outbill.ui.version'},
         {'module': 'bms-server', 'versiontag': 'bms.inbill.ui.version'},
         {'module': 'bms-server', 'versiontag': 'bms-external-api'},
         {'module': 'bms-server', 'versiontag': 'bms.external.api'},
         {'module': 'bms-server', 'versiontag': 'bms.version'},
         {'module': 'bms-server', 'versiontag': 'bms.inbill.version'},
         {'module': 'bms-server', 'versiontag': 'bms.outbill.version'},
         {'module': 'bms-server', 'versiontag': 'bms.commom.version'},
         {'module': 'bds-server', 'versiontag': 'bds.basedict.api.version'},
         {'module': 'bds-server', 'versiontag': 'bds.version'},
         {'module': 'bds-server', 'versiontag': 'bds.basedict.api'},
         {'module': 'bds-server', 'versiontag': 'bds-external-api.version'},
         {'module': 'bds-server', 'versiontag': 'bds-project.version'},
         {'module': 'bds-server', 'versiontag': 'bds-basedict-ui.version'},
         {'module': 'bds-server', 'versiontag': 'bds-basedict-util.version'}]

df = pd.DataFrame([{'module': 'bms-server', 'versiontag': 'bms-ui'},
                   {'module': 'bms-server', 'versiontag': 'bms-123'},
                   {'module': 'bms-server', 'versiontag': 'bms-456'},
                   {'module': 'bds-server', 'versiontag': 'bds-ui'},
                   {'module': 'bds-server', '': 'bds-123'}])

for l2 in list2:
    module = l2.get('module')
    versiontag = l2.get('versiontag')
    # print(module, ':', versiontag)

groupd = groupby(list2, key=lambda x: x['module'])
# ls3 = {k: v2 for v2 in v1 for k, v1 in groupd}

dicts = {k: [l_v.get('versiontag') for l_v in v] for k, v in groupby(list2, lambda x: x['module'])}
print('dicts', dicts)

# ls = groupby(list, key='module')
# for k, v in ls:
#     print('k', k)
#     print('v', v)

# ls = [k for k, g in groupby('AAAABBBCCDAABBB')]
# print(ls)
#
# ls2 = [list(g) for k, g in groupby('AAAABBBCCD')]
# print(ls2)


key = lambda x: 'module'
print(key)
