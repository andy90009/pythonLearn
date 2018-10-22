
# def 定义一个函数，参数和返回值不是必须的
def listsum(l):
    result = 0
    for i in l:
        result = result + i
    return result
r = listsum([1,2,3,4])
print (r)

def hi():
    print ('hi,python')
hi()

# 默认参数
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
def Cube(x=5):
    return x**3
print (Cube())                  # 打印默认参数5的立方
print (Cube(2))                 # 打印传入的参数2的立方

# 多个默认参数
def zoe(x=1,y=2,z=3):
    return x+y+z;
print (zoe())                   # 无传入参数时，使用默认参数
print (zoe(3,3))                # 顺序传入参数：x=3,y=3
# zoe(,,5) 不能这样使用，会报错
# 指定参数传值
def eva(x=None,y=None,z=None):
    if x == None:
        x= 1
    if y == None:
        y = 2
    if z == None:
        z = 3
    return x + y + z;
print (eva())                  # 使用默认参数
print (eva(None,None,9))       # 使用传入参数 z=9

# 函数参数的传递方式
print ('----参数的传递方式----')
def fun(x,y,z):
    return x + y - z;

print (fun(1,2,3))             # 顺序传入
print (fun(z=1,y=2,x=5))       # 根据参数名传入

# 数据类型转换
print ('----数据类型转换----')

print (int('123'))
print (int(12.56))            # 只取整数位
print (str(123))

print (hex(255))
print (hex(1000))

# 请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回
# 函数体内没有return 将返回 None，相当于 return None

# 空函数
def nop():
    pass

# 实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
# pass 还能放在其他语句中，例如：
def test(age):
    if age >= 18:
        pass
    return None
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#my_abs('A')

# 函数返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100,100,1,math.pi/6)
r = move(100,100,1,math.pi/6)
print (x,y)
print (r)               # 其实函数返回多个值 就是一个tuple

def quadratic(a, b, c):
    derta = b*b - 4*a*c
    if derta > 0:
        return (-b+math.sqrt(derta))/2*a,(-b-math.sqrt(derta))/2*a
    if derta == 0:
        return (-b)/2*a,(-b)/2*a
    else:
        print ('此一元二次方程无实数解')
        return None

# python中默认参数最大的坑
def add_end(l=[]):
    l.append('end')
    return l

# 正常调用时，似乎结果不错
print (add_end([1,2,3]))               # [1,2,3,'end']
print (add_end(['x','y','z']))         # ['x','y','z','end]

# 使用默认参数调用时，一开始也是对的
print (add_end())                      # ['end']
# 再次调用时，结果就不对了
print (add_end())                      # ['end','end']
print (add_end())                      # ['end','end','end']

# 解释Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 所以，默认参数必须指向不变对象

# 上述例子，可以使用不变对象None来实现
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 无论调用多少次，都不会有问题
print (add_end2())
print (add_end2())

# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
# 调用的时候，需要先组装出一个list或tuple
print (calc([1,2,3]))
print (calc((1,3,5,7)))
# 利用可变参数，让调用变得简单
# 在函数内部，number接收到的是tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print (calc(1,2,3))
print (calc(1,3,5,7))

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print ('name:', name,'age:', age, 'other:', kw)
person('andy',28)
person('eva',29,city='chengdu')
# 也可以先组装一个dict，作为关键字参数传入
extra = { 'city':'chengdu', 'job':'coder'}
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('zoe',28,**extra)

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
def person2(name,age,**kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print ('name:', name, 'age:', age, 'other:', kw)

# 但是仍然可以传入不受限制关键字参数，例如
person2('andy',28,city='chengdu',job='cmcc',zipcode=123456)

# 如果想要限制关键字参数的名字，就可以使用命名关键字参数
# 只接收city 和 job 这两个作为关键字参数

# def person3(name,age,*,city,job):
#     print ('name:', name, 'age:', age, 'city:', city, 'job:', job)
# person('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person4(name, age, *args, city, job):
#     print(name, age, args, city, job)
# person4('andy',28,'lalala',city='chengdu',job='cmcc')

# 总结
'''
位置参数: def power(x) 必须传入有且只有的一个参数x
         def power(x,n) 两个都是位置参数
默认参数: def power(x,n=2) 调用时可以power(5) power(5,3)
         注意：默认参数必须指向不变对象
可变参数: def calc(*number) 调用时 calc(1,2) calc(1,2,3) calc()
         注意：可变参数传入的是一个tuple
关键字参数: def person(name,age,**kw) 调用时 person('andy',28,city='chengdu')
          注意：关键字参数传入的是一个dict
命名关键字参数: def person(name, age, *, city, job) 
        注意：关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
             命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
        调用: person('andy',28,city='chengdu',job='cmcc')
参数组合：可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
         注意：顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

'''

# 递归函数

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print (fact(5))

# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 例如 fact(1000)

# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况

def fact2(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print (fact2(5))

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，
# Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出

# ??? 醉了












