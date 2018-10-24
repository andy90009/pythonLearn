
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
