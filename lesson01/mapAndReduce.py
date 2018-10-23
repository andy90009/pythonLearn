
# map/reduce

# Python内建了map()和reduce()函数

# map()
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

# 举例说明，比如我们有一个函数f(x)=x2，
# 要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print (list(r))

# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list

# 你可能会想，不需要map()函数，写一个循环，也可以计算出结果
L = []
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(x))
print (L)

# 但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
# 所以，map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

print (list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 只需要一行代码

# reduce()
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

from functools import reduce

# 例1
def add(x,y):
    return x + y

print (reduce(add,[1,3,5,7,9]))            # add(add(add(add(1,3),5),7),9)

# 例2
def fn(x,y):
    return x*10 + y

print (reduce(fn,[1,3,5,7,9]))            # fn(fn(fn(fn(1,3),5),7),9)

# 例3
# 例1，例2本身没多大用处
# 但是如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    def fn(x, y):
        return x*10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))

print (isinstance(str2int('167'),int))
print (str2int('167') == 167)


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

