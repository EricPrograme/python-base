# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 17:23


"""

导包

导入packege

导入包的注意事项：

import packege
import calc
使用import方式进行导入时，只能跟包名或者模块名

from packege import module_A
from packege.module_A import a
使用from..import可以导入包，模块，函数，变量

"""



# import packege.module_A

# as 别名
import packege.module_A as ma
# print(packege.module_A.a)

print(ma.a)

