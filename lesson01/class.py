
# 类和实例
# 类是抽象的模板，而实例是根据类创建的具体的对象
#

class Student(object):

    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # 数据封装
    def print_score(self):
        print ('%s : %s' %(self.__name, self.__score))

    # 封装的另一个好处是可以给Student类增加新的方法
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # 如果外部代码要获取name和score怎么办？
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 外部代码改变name和score
    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')




bart = Student('bart', 59)
print (bart)

# 类的成员变量 + '__' 是私有变量，外部不能访问
# print ('bart.name: %s, bart.score: %s' %(bart.__name, bart.__score))

bart.print_score()
x = bart.get_grade()
print (x)

#

stu = Student('andy', 99)
print ('stu.name: %s, stu.score: %s' %(stu.get_name(), stu.get_score()))

stu.set_name('zoe')
stu.set_score(97)
print ('stu.name: %s, stu.score: %s' %(stu.get_name(), stu.get_score()))


# 继承和多态

class Animal(object):

    def run(self):
        print ('Animal is running')

class Dog(Animal):

    def run(self):
        print ('Dog is running')

class Cat(Animal):

    def run(self):
        print ('Cat is running')


dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态

# 要理解什么是多态，我们首先要对数据类型再作一点说明。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# 任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
# 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
# 就会自动调用实际类型的run()方法，这就是多态的意思

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
# 否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):

    def run(self):
        print ('start....')

run_twice(Timer())

# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

# Python的“file-like object“就是一种鸭子类型。
# 对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象


# 获取对象信息

# type()

print (type(123))
print (type('string'))
print (type(None))

print (type(abs))
print (type(dog))

print (type(123) == int)
print (type('str') == str)

# 判断基本数据类型可以直接写int，str等，
# 但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量

import types

print (type(run_twice) == types.FunctionType)
print (type(abs) == types.BuiltinFunctionType)
print (type(lambda x: x) == types.LambdaType)
print (type(x for x in range(1, 10)) == types.GeneratorType)

# isinstance()

# 对于class的继承关系来说，使用type()就很不方便。
# 我们要判断class的类型，可以使用isinstance()函数。

'''
总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
'''

# dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print (dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，下面的代码是等价的

print (len('ABC'))
print ('ABC'.__len__())

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法

# slots
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# def Student(object):
#     __slots__ = ('name', 'age')

class Teacher(object):
    __slots__ = ('__name', '__age')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

t = Teacher('zoe',29)


# @property
# 上面的 get set调用方法又略显复杂，没有直接用属性这么直接简单
# Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Manager(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be Integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    @property                       # 如果只有get 没有set 就只是一个可读属性
    def name(self):
        return self._name

m = Manager()
m.score = 60                # 相当于 m.set_score(60)
print (m.score)             # 相当于 m.get_score()
#m.score = 1000              # 报错
