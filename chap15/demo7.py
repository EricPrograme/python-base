# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""

os文件操作

os模块是与操作系统相关的一个模块
"""

import os

# 打开记事本
# os.system('notepad.exe')
# os.system('calc.exe')

# 直接调用可执行文件
# 打开本机钉钉
# os.startfile("D:\\Program Files (x86)\\DingDing\\DingtalkLauncher.exe")

# 获取当前工作目录
print(os.getcwd())
lst = os.listdir('../chap15')
print(lst)

# 创建目录
# os.mkdir("newdir2")

# 创建多级目录，创建A目录下B,B目录下，C目录
# os.makedirs('A/B/C')


# 删除目录
# os.rmdir("newdir2")
# 删除多级目录
# os.removedirs('A/B/C')

# 将paht设置为当前的工作目录
os.chdir("E:\\eric\\python\\chap15")
print(os.getcwd())