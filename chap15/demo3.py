# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/28 11:19


"""
文件读写

"""
# file = open('a.txt', 'r',encoding='utf-8')

# 读
# print(file.read(2))
# print(file.readline())
# print(file.readlines())
# file.close()


print("-------写，追加-----------")
file2 = open("c.txt", 'a', encoding="utf-8")
# file2.write('Hello')
lst = ['java', 'python', 'c']
file2.writelines(lst)
file2.close()


print("---------------------------")
file3 = open("c.txt", "r", encoding="utf-8")
# seek 跳过2个字节来读取
file3.seek(2)
print(file3.read())
print(file3.tell())
file3.close()

file4 = open("d.txt",'w', encoding='utf-8')
file4.write("jerry")
file4.flush()

file4.write('tom')
file4.close()