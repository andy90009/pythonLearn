
# 定制类

# __str__ 返回用户看到的字符串
# __repr__ 返回开发者看到的字符串

class Student(object):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Student object (name: %s)' % self._name

    __repr__ = __str__

s = Student('zoe')
print ('ss',s)
s           # 控制台看不见，命令行可以

# __iter__

# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环

class Fib(object):

    def __init__(self):
        # 初始化两个计数器 a,b
        self._a = 0
        self._b = 1

    # 实例本身就是迭代对象，故返回自己
    def __iter__(self):
        return self

    # 迭代对象的next方法
    def __next__(self):
        self._a, self._b = self._b, self._a + self._b   # 计算下一个值
        if self._a > 1000:
            raise StopIteration     #退出循环
        return self._a
    #
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a+b
        return a

for n in Fib():
    print (n)

# __getItem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 比如，取第5个元素
# print (Fib()[5])

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
print (Fib()[5])

from datetime import datetime

print (datetime.now().timestamp())
