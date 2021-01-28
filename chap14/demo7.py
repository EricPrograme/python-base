# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 17:23


"""
 python中常用的内置模块

"""

import sys
import time
import urllib.request
import math


print(sys.getsizeof(24))
print(sys.getsizeof(48))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))


print(urllib.request.urlopen('http://www.baidu.com').read())


print(math.pi)


