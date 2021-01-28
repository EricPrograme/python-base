# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
文件读写

"""
# 读
file = open('a.txt', 'r', encoding='utf-8')
print(file.readlines())
file.close()


# 写
file2 = open("b.txt", "w", encoding="utf-8")
file2.write('hello，python !')
file2.close()

# 追加 a
file2 = open("b.txt", "a", encoding="utf-8")
file2.write('hello，python !')
file2.close()


# 二进制打开,读写
src_file = open('alien.bmp', 'rb')
target_file = open("copybmp.png", 'wb')
print(target_file.write(src_file.read()))
target_file.close()
src_file.close()