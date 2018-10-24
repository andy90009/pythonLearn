
# 匿名函数
# 关键字lambda表示匿名函数,冒号前面的x表示函数参数

a = list(map(lambda x: x*x, [1, 2, 3, 4, 5]))
print (a)

f = lambda x: x*x
# 注意lambda 返回的是一个函数
print (f)
# 5 就是传入的参数 x
print (f(5))

L = list(filter(lambda x: x%2 == 1, range(1,20)))
print (L)