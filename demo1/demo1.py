def hi(name="eric"):
    return "hi " + name


print('h1() = ',hi())
# output: 'hi eric'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print('greet() = ',greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
# print('del hi()',hi())
# outputs: NameError

print('del greet() = ',greet())
# outputs: 'hi yasoob'