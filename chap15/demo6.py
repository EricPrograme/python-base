# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
with语句
读写二进制文件

"""


with open('alien.bmp', 'rb') as src_file:
    with open('copybmp2.png', 'wb') as target_file:
        target_file.write(src_file.read())
