# Author: hmchen
# DATE  : 2021/3/13 21:31



def test_ages(*args):
    print(args,type(args))
    pass




test_ages('name','age','sex')



def function(**kwargs):
    print(kwargs,type(kwargs))


function(a=1, b=2, c=3)