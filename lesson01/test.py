print ('hello python')  # 单行注释
# name = input('请输入你的用户名:')
# print ('刚刚输入的用户名为：' + name)

'''
多行注释,貌似python3不用写utf-8
'''
t = ['1', '2', '3']
for i in t:
    print (i)

print (3 * 5 / 2)
print (3.0 * 5.0 / 2)
# 2的3次方
print (2 ** 3)

import math

print (math.cos(0.5))
print (math.exp(3))
print (math.hypot(3, 4))  # 求直角边为3，4的斜边长度
print (math.fmod(3, 4))  # 求余运算，3/4 余数为3
print (99 ** 99)
print (4 / 2)

# ^	按位异或运算符：当两对应的二进位相异时，结果为1
# 左移一位 相当于 乘以 2**0; 右移动一位 相当于 除以 2**0; 在数据没有溢出的情况下

print (4 >> 2)
print (4 << 2)
print (-61 << 2)

print ('****************************************************')
str1 = 'hello,python!'
str2 = 'hello'
str3 = 'Python is wonderful'
# 字符串的第一个字母大写 注意只有第一个字母大写
print (str1.capitalize())
# 获取字符串某一字符串的数目
print (str1.count('p'))
# 获取字符串某一字符的起始位置 -1表示没找到
print (str1.find('p'))
# 分割字符串 返回一个数组,如果字符串中没有',' 则返回该字符串的数组形式
print (str1.split(','))
print (str2.split(','))
print (str1.split())
print (str3.split())
print (str3.split(None, 1))  # 以空格分割，但是只分割一次
print (str3.split(None, 0))
print (str3.split(','))
# 首字母大写, 注意：所有单词的首字母大写
print (str1.title())
# 获取字符串的长度
print (len(str1))
# 连接字符串 注意：以str1为分隔符，连接参数中的每一项
print (str1.join('HM'))

# 上述操作不会改变str1本身的内容，返回修改后的字符串

print ('*****************list[]:列表***********************')

list1 = []
print (list1)
# 结果为None?
list1.append(1)
print (list1)
# 计算2在list1中出现的次数
print (list1.count(2))
# 向list1中添加一个列表
list1.extend([2, 3, 4, 5])
print (list1)
# 获取5在list1中的位置
print (list1.index(5))
# 从位置序号2开始插入，其他成员以此后移
list1.insert(2, 6)
print (list1)
# 删除位置序号为2的元素
list1.pop(2)
print (list1)
# 删除列表中值为5的第一个元素
list1.insert(2, 5)
print (list1)
list1.remove(5)
print (list1)
# 列表排序
list1.insert(2, 8)
print (list1)
list1.sort()
print (list1)

print ('************************tuple():元组**************************')

# tuple中元素一旦确定，就无法改变
tuple1 = ('a', 'b', 'c')
# 在list1中插入一个元组
list1.insert(2, tuple1)
print (list1)
# 访问list1中第三个元素
print (list1[2])
# 使用分片 序号1:4 不包含序号为4的成员
print (list1[1:4])
#
print (tuple1[2])
# 使用分片 得到1:2 不包含序号为2的成员
print (tuple1[1:2])

print ('**************************dict{}:字典*****************************')

# dict{}:字典，无序，key-value，通过key来访问成员。value的值是可变的。

dict1 = {'apple': 2, 'orange': 3}
print (dict1)
# 复制字典
dict2 = dict1.copy()
print (dict2)
# 增加一项
dict1['banana'] = 5
print (dict1)
# 获取字典dict1的成员列表 返回dict_items([('apple', 2), ('orange', 3), ('banana', 5)])
print (dict1.items())
# 删除key='apple',并返回其值
print (dict1.pop('apple'))
print (dict1)
# 删除key='apple',如果没有'apple',则返回3
print(dict1.pop('apple', 3))
# 获取dict1的key的列表 返回的是一个list
print (dict1.keys())
# 获取dict1的value的列表
print (dict1.values())
# 更新dict1某个key对应的value ,如果没有，则添加
dict1.update({'banana': 10})
print (dict1)
dict1.update({'apple': 20})
print (dict1)
# 清空
dict1.clear()
print (dict1)

print ('*************************file:文件************************************')

# 文件也可以看成python的数据类型
# python内置函数open(filename,mode) filename:文件名 mode:可选参数，指文件的打开方式
# mode: 'r'--只读 'w'--只写 'b'以二进制方式打开 等等

# 为啥绝对路径报错，找不到？？
# file = open('/Users/liaohaibo/desktop/coding/learn/pythonLearn/leasson01/pylearn.txt','w')
fileW = open('./pylearn.txt', 'w')
fileW.write('python\n')

# 定义一个空列表
# range(10) 返回list[0,1,2,3,4,5,6,7,8,9]
# writelines() 向文件中写入一个列表
# write() 写入字符串
# read() 将整个文件读入字符串中
# readline() 读入文件的一行到字符串中
# readlines() 将整个文件按行读入列表中
a = []
for i in range(10):
    s = str(i) + '\n'
    a.append(s)
fileW.writelines(a)
# 必须要关闭，否则读出来为空
fileW.close()
fileR = open('./pylearn.txt', 'r')
b = fileR.read()
print (b)
# 关闭文件
fileR.close()
fileR2 = open('./pylearn.txt')
c = fileR2.readlines()
print (c)
fileR2.close()

print ('***********************if语句******************************')

# if<条件>:
#   <语句>
# elif<条件>:
#   <语句>
# else:
#   <语句>

a = 1
b = 2
if a == b:
    print ('true')
else:
    print ('false')

if a < b:
    print ('true')
else:
    print ('false')

print ('************************for循环******************************')

'''
for <> in <对象集合>
    if<条件>:
        break        #终止循环
    if<条件>:
        continue     #使用continue调过其他语句，继续循环
    <其他语句>
else:
    <>



'''

for i in [1, 2, 3, 4, 5, ]:
    if i == 6:
        break
    if i == 2:
        continue
    print (i)
else:
    print ('all')
