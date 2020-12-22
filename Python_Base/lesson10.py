"""
python·lesson10
继承，多继承和魔术方法
-继承
-多继承
-魔术方法
"""
#继承
#最好不要继承超过三类
class Rec(object):  #object顶级父类 是根类……有该项的也是父类
    pass

r = Rec()
print(dir(r))       #输出根类魔法方法

class Father(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('{}你去哪'.format(self.name))

    def run(self):
        print('跑步')


class Mother(object):           #多继承
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('{}路上小心'.format(self.name))

    def make_dinner(self):
        print('做饭')

class Son(Father,Mother):       #继承都有：先左边
    pass
    # def say_hello(self):
    #     print('{}say hi'.format(self.name))     #重写
    #
    # def play_football(self):
    #     print('{} like playing football'.format(self.name))
    # pass

s = Son('小明',10)
print(dir(s))           #输出根类魔法方法，且继承父类定义方法
s.say_hello()
s.run()
s.make_dinner()

print(Son.__bases__)
print(Father.__bases__)
print(object.__bases__) #输出为空

print(Son.__mro__)      #输出继承路径 == 解析路径

class Father(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('{}你去哪'.format(self.name))

    def run(self):
        print('跑步')


        print('做饭')

# class Son(Father,Mother):       #继承都有方法：先左边
#思想:mix-in(拼积木，组装）
#思想:直线继承，父类比子类全面

print('abc'+'ghi')  #同样的符号，不同的输出含义；实际都是在使用__add__这个魔术方法
print(1+2)
print(dir(18))
print(dir('abc'))
a = 10
b = 20
print(a + b)
print(a.__add__(b))

#
class Rectangle(object):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def get_area(self):
        print(self.length * self.width)

    def __add__(self, other):
        length = self.length + other.length
        width = self.width + other.width
        result = Rectangle(length, width)
        return result

a = Rectangle(20,10)
b = Rectangle(50,30)
new_rec = a + b     #右式a.__add__(b),是Rectangle中新定义的

print(type(new_rec))
new_rec.get_area()
#魔术方法——可以自定义，改装，满足个性化
#_str_简介有用
#_retr_接近开发源

class Test(object):
    '''
    这是一个文档
    '''
    def hi(self):
        print('hi')

    def __call__(self, *args, **kwargs):    #可以直接调用的魔术方法
        self.hi()

t = Test()
t()

print(Test.__class__)   #输出类名
print(Test.__dict__)    #输出全部数学，返回属性和属性值 键值对形式
print(Test.__doc__)     #打印类中文档（段引用部分）
class Y(object):
    def say_hello(self):
        return '你去哪'

class F(Y):
    def say_hello(self):
        return '臭小子你去哪'

    def run(self):
        print('跑步')

class M(Y):           #多继承
    def say_hello(self):
        print('nihao ')



class Son_1(F):
    def say_hello(self):
        my_str = '不喜欢这句话：'
        new_str = super().say_hello()   #super().该方法直接指向父类（上一类），调用；多继承例外:见Son_2.__mro__输出
        print(my_str + new_str)

sa = Son_1()
sa.say_hello()

class Son_2(F,M):
    def say_hello(self):
        super().say_hello()

sa = Son_2()
sa.say_hello()
print(Son.__mro__)  #输出继承为：先子，再父，再母*，再爷
#super可以调用父类，父类也可以使用super；可以通过__mor__属性或者mro方法来查看类的继承关系

#继承矩形类，生成正方形。
class Rectangle(object):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def __add__(self, other):
        length = self.length + other.length
        width = self.width + other.width
        result = Rectangle(length, width)
        return result

    def get_area(self):
        print(self.length * self.width)

class Square(Rectangle):
    def __init__(self,side_length ):
        super().__init__(side_length,side_length)

    def __call__(self, *args, **kwargs):
        return self.get_area()

    def __str__(self):
        return  '这个正方形的边长是：{}'.format(self.length)

s = Square(10)
print(s())
print(s)
s()