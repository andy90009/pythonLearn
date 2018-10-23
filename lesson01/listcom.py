
# 列表生成式

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (list(range(1,11)))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10] ?
L = []
for x in range(1, 11):
    L.append(x*x)
print (L)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
L1 = [x*x for x in range(1, 11)]
print (L1)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L2 = [x*x for x in range(1,11) if x%2 == 0]
print (L2)

# 还可以使用两层循环，可以生成全排列
L3 = [m+n for m in 'xyz' for n in 'abc']
print (L3)

# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
L4 = [d for d in os.listdir('.')]
print (L4)

# for循环其实可以同时使用两个甚至多个变量
# 比如dict的items()可以同时迭代key和value
D1 = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in D1.items():
    print (k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list
L5 = [k+'='+v for k,v in D1.items()]
print (L5)

# 把一个list中所有的字符串变成小写
L6 = ['Hello', 'World', 'IBM', 'Apple']
L7 = [s.lower() for s in L6]
print (L7)

# 如果list中既包含字符串，又包含整数，
# 由于非字符串类型没有lower()方法，所以列表生成式会报错
L8 = ['Hello', 'World', 18, 'Apple', None]
L9 = [s.lower() for s in L8 if isinstance(s,str)]
print (L9)
