
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

print (fun(1,2,3))
print (fun(z=1,y=2,x=5))



