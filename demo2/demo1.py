# Author: hmchen
# DATE  : 2021/3/1 22:23


# 打印 1~100 的基数
#  1~100 的基数有多少个
# 计算1~100有多少个基数的计算时长
import time


def jishutime(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        total = t2-t1
        print(total)
    return wrapper


# 是否是基数
def is_jishu(num):
    if num == 0:
        return False
    else:
        if num % 2 != 0:
            return True




# 基数
@jishutime
def jishu():
    for num in range(1, 2000):
       if is_jishu(num):
           print(num)





# jishutime()
jishu()