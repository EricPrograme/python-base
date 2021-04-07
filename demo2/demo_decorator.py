import time


"""

def xx1(被装饰函数）：
     def xx2（如果被装饰函数有参数那么输入）：
             xxxxxxxxxxxxxxx
             被装饰函数（如果被装饰函数有参数那么输入）
             xxxxxxxxxxxxxxx
             # 如果被装饰函数中含有reture则需要返回被装饰函数
             # 没有则不需要
       reture xx2

"""


def display_time(func):
    """ 装饰器 """
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("total time :{:.4} s".format(t2 - t1))
        return result
    return wrapper


def is_prime(num):
    # 判断是否是质数,质数大于等于2 不能被它本身和1以外的数整除
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# def is_prime(num):
#     if num < 2:
#         return True
#     elif num == 2:
#         return False
#     else:
#         for i in (2, num):
#             if num % i == 0:
#                 return False
#         return True


@display_time
def prime_nums():
    # t1 = time.time()
    for i in range(2, 20000):
        if is_prime(i):
            print(i)
    # t2 = time.time()
    # print(t2 - t1)


@display_time
def count_prime_nums(maxnum):
    count = 0
    for i in range(2, maxnum):
        if is_prime(i):
            count = count + 1
    return count


# prime_nums()

count = count_prime_nums(10000)
print('count=', count)


