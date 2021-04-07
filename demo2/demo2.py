# Author: hmchen
# DATE  : 2021/3/13 22:04


class Foo():
    print('foo')


class Coo():
    print('coo')



def break_func():
    add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
    for i in add:
        if i ==',':
            break
        print(i,end="")
    print("\n执行循体外的代码")

def continue_func():
    add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
    for i in add:
        if i == ',':
            print('\n')
            continue
        print(i,end="")
    print("\n执行循体外的代码")

continue_func()
# break_func()


a=10
b=20
c=30
g={'a':7, 'b':111} #定义一个字典
t={'b':100, 'c':10} #定义一个字典
print(eval('a+b+c', g, t)) #定义一个字典 116