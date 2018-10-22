
# slice 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素，应该怎么做

# 笨办法1：
print ([L[0], L[1], L[2]])

# 笨办法2：
r = []
n = 3
for i in range(n):
    r.append(L[i])
print (r)

# 使用slice操作符
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print (L[0:3])
# 如果第一个索引是0，还可以省略
print (L[:3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print (L[-1:])   # 相当于-1~0 0不可写上,同样不包括最后的索引
print (L[-2:-1])

Num = list(range(100))
print (Num)

# 取前10个数
print (Num[0:10])

# 取后10个数
print (Num[-10:])

# 每5个取1个
print (Num[::5])

# 复制一个list
print (Num[:])

# tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple

t = (0,1,2,3,4,5)
print (t[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串

print ('ABCDEFG'[:3])
print ('ABCDEFG'[::2])

# print (' hello '[:])
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])          # 去掉首部空格
    else:
        return trim(s[:-1])        # 去掉尾部空格
print (trim(' hello '))
print (trim('') == trim('   '))
