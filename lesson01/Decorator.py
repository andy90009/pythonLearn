
# 装饰器 Decorator

# 函数也是一个对象，函数对象也可以赋值为变量
# 所以，通过变量也能调用该函数


def now():
    print ('now: 2018-10-22')

f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字

print (now.__name__)
print (f.__name__)

print ('--------decorator--------')
# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下


def log(func):
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def my_now():
    print ('my_now: 2018-10-22')

my_now()

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数
# 我们要借助Python的@语法，把decorator置于函数的定义处
# 调用my_now()函数，不仅会运行my_now()函数本身，还会在运行my_now()函数前打印一行日志

'''
由于log()是一个decorator，返回一个函数，所以，原来的my_now()函数仍然存在，
只是现在同名的my_now变量指向了新的函数，
于是调用my_now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本

import functools

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print ('%s %s()' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('excute')
def my_now2():
    print ('my_now2: 2018-10-22')

my_now2()

print (my_now2.__name__)