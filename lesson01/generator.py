
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，一边循环一边计算的机制，称为生成器：generator

# 创建generator
# 方法1：只要把一个列表生成式的[]改成()，就创建了一个generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator

L = [x * x for x in range(10)]
print (L)
g = (x * x for x in range(10))
print (g)

# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
print (next(g))
print (next(g))
print (next(g))

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值,
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误,
# 正确的方法是使用for循环，因为generator也是可迭代对象。
# 所以，我们创建了一个generator后，基本上永远不会调用next()，
# 而是通过for循环来迭代它，并且不需要关心StopIteration的错误
for n in g:
    print (n)

# generator非常强大。
# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现

# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):                           # max表示数列里数的个数
    n, a, b = 0, 0, 1
    while n < max:
        #print (b)
        yield b
        a, b = b, a+b                   # 相当于 t=(a,a+b) a=t[0] b=t[1]
        n = n + 1
    return 'done'
fib(3)

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator

# 最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行

# 例：
def odd():
    print ('step1')
    yield 1
    print ('step2')
    yield (2)
    print ('step3')
    yield (5)

o = odd()
next(o)
next(o)
next(o)

for n in fib(6):
    print (n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

gg = fib(6)
while True:
    try:
        x = next(gg)
        print ('gg:', x)
    except StopIteration as e:
        print ('return value:', e.value)
        break

# 练习 杨辉三角
# 思路
# 某一行的为list b
# 则下一行的计算为 首尾添加个0 然后加起来
#   0 b1 b2
# + b1 b2 0

from operator import *

def triangles():
    L = [1]
    while True:
        yield L
        a = [0] + L
        b = L + [0]
        L = list(map(add,a,b))

# 测试用例
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

for i in range(2):
    print (i)
