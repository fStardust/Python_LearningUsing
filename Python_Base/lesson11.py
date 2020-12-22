"""
python·lesson11
new方法、定制属性访问、描述符与装饰器
-new方法
-定制属性访问
-描述符
-装饰器
"""
#new方法;创建实例，分配空间，cls指向类本身；init，初始化,self指向实例本身
class Test(object):
    def __init__(self):
        print('我是init方法')
        pass

    def __new__(cls, *args, **kwargs):  #new方法原先既有内容，若改写pass掉，则不生成实例
        print('我是new方法')
        print(cls)
        return super().__new__(cls)     #推荐使用super调用父方法；必须有该方法调用父类以生成实例
        pass

t = Test()
print(t)    #根据输出得知先运行new方法，再运行init方法
a = Test()
b = Test()
print(a is b)
print(id(a))
print(id(b))
#单例模式，可以用于重复读取数据（配置文件）模式时——多次读取但依旧只用了一个实例；仅在第一次创建新实例；继承的子类也是单例
class Test(object):
    __instance = None   #私有属性（只在类中使用）；保存实例的变量

    def __init__(self):
        print('我是init方法')
        pass

    def __new__(cls, *args, **kwargs):  #
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

a = Test()
b = Test()  #第二次运行返回的还是原先的实例
print(a is b)
print(id(a))
print(id(b))

#定制属性访问
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

    def __getattr__(self, item):    #调用该类时，如果有该属性则不运行；若无则运行:见80行
        print('没有该属性')

rec = Rectangle(15,10)
print(rec.length)
print(hasattr(rec,'length'))    #判断某实例是否有该实例属性

print(getattr(rec,'length'))    #获取该属性方法
print(rec.__getattribute__('length'))   #

print(setattr(rec,'length',2))  #有该属性就改值；无该属性就添加
print(rec.length)
print(rec.__setattr__('length',4))      #同上
print(rec.length)

delattr(rec,'length')           #删除该属性
print(hasattr(rec,'length'))
print(rec.__delattr__('width'))        #同上
print(hasattr(rec,'width'))

del rec                         #删除该实例
re = Rectangle(10,20)
print(re.hihi)

#描述符 通过魔术方法让开发人员更加灵活的控制类的表现形式
class MyAttr(object):       #python描述符是一个‘绑定行为’的对象属性，通过方法（__get__();__set__();__delete__()）重写属性的访问
    def __get__(self, instance, owner): #访问（获取）时触发
        print('hello world')
        print('happy')
        print('H')

    def __set__(self, instance, value): #赋值（修改）时触发
        print('happy new year')

    def __delete__(self, instance): #删除时触发
        print('end')

class MyClass(object):
    attr = MyAttr()
    normal_attr = 'abc'

c = MyClass()
print(c.attr)
print(c.normal_attr)
c.attr = 100
del c.attr

#装饰器-闭包——高内聚（同功能下相同内容联系紧密），低耦合（各功能之间联系松散）
#不修改模块内部，但改变修改结果


#装饰器
def modify(func):
    def wrapper():
        result = func()
        return result + '，她好看'
    return wrapper  #带（）指的是调用函数，返回函数运算结果；不带是调用函数本身

@modify #girl用了modify这个函数来装饰，仅影响紧接着的函数
def girl():
    return '这是一个女孩'

# girl = modify(girl) #替换函数内容 被@modify给替代
print(girl())

#python内置三个装饰器：
#@property 就像访问属性
#@staticmethod 静态方法和class类断开联系
#@classmethod 类方法
class Rectangle(object):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    @property   #对属性做特殊处理
    def get_area(self):
        print(self.length * self.width)

    @classmethod    #类方法，由类进行调用
    def hello(cls):
        print('hello')

    @staticmethod   #静态方法 既可以类调用·152，也可使通过实例调用·153
    def hi():       #不需串联的方法；存放方法
        print('hi')


rec = Rectangle(10,8)
print(rec.get_area)
Rectangle.hello()
Rectangle.hi()
rec.hi()

#类装饰器；call
class MyClass:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(*args)   #当函数有参数时，应被装饰器中调用处调用；故在此也要加入参数（不定长参数即可）

@MyClass
def test(name):
    print('name: {}'.format(name))

test('lili')

import time

def run_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        r_time = time.time() - start_time
        print(r_time)
        return result
    return wrapper

@run_time
def say_hello():
    print('hello')

say_hello()