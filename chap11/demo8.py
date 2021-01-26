# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/25 16:36

"""

Traceback 模块

"""
import traceback
try:
    print("-----------------------")
    print(10/0)

except:
    traceback.print_exc()

