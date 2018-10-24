
# 函数作为返回值

# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的

def calc_num(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数：

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)

# 调用lazy_sum,返回的是求和函数，不是结果
print (f)
# 调用f(),返回的是结果
print (f())

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 注意 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print (f1 == f2)

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易

# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print (f1())
print (f2())
print (f3())

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 如果一定要用循环呢
#
def count1():
    fs = []
    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))         # f(i) 立刻执行 因此i的当前值被传入f()
    return fs
f11, f22, f33 = count1()
print (f11())
print (f22())
print (f33())

# 还不是懂？
# 再来看看

# 闭包的概念
# 在一个内部函数中，对外部作用域的变量进行引用，(并且一般外部函数的返回值为内部函数)，那么内部函数就被认为是闭包
# 举个例子

# 在函数startAt中定义了一个incrementBy函数，
# incrementBy访问了外部函数startAt的变量，
# 并且函数返回值为incrementBy函数

def startAt(x):
    def incrementBy(y):
        return x + y
    return incrementBy

a = startAt(1)
print ('function:', a)                          # function: <function startAt.<locals>.incrementBy at 0x108ef9048>
print ('result:', a(1))                         # result: 2

# 从打印结果可以看出 a其实就是一个函数
# 并且 a就是 incrementBy 而不是 startAt
# 不难理解 因为return回来的就是 incrementBy

# 闭包无法修改外部参数的值

def outerfunc():
    x = 1
    def innerfunc():
        x = 0
        print ('inner x:', x)                       # 0
    print ('before called innerfunc x:', x)         # 1
    innerfunc()
    print ('after called innerfunc x:', x)          # 1

outerfunc()

