# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
列出指定目录的所有子目录下的文件


"""

import os

path = os.getcwd()
lst_files = os.walk(path)
# print(lst_files)
for dir_path, dir_name,file_name in lst_files:
    print("dir_path ：", dir_path)
    print("dir_name ：", dir_name)
    print("file_name ：", file_name)
    print('-----------------------------------------------------')
    for dir in dir_name:
        print(os.path.join(dir_path,dir))
    print("--------------------------------------")
    for file in file_name:
        print(os.path.join(dir_path,file))


