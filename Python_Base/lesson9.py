"""
python·lesson9
类的定义属性和方法
-类的定义和属性
-类的方法
-类的初始化和析构
"""

#类的定义和属性
#驼峰命名规则
class MyClass(object):
    my_var = 'abc'
    _old_var = 'fer'
    __new_var = 123
    pass

a = MyClass()   #生成一个实例
b = MyClass()
#类是一个独立存放的
print(MyClass.my_var)   #调用类属性
MyClass.new_ver = 100
print(MyClass.new_ver)
a.instance_ver = 10
print(a.instance_ver)
print(a.my_var)
#类：是一类事物的抽象——共性
#实例：具体个体，是该类的具体表现
#print(MyClass.__new_var)    #强制性私有属性，外部不可使用
print(MyClass._old_var) #非强制性私有属性，外部可使用，但使用不报错


#类的方法-描述行为
#在类中的函数-特殊函数
#文件-模块-类-函数
class MyClass(object):
    def my_func(self):  #self代表实例本身
        print(self.var)

ins_1 = MyClass() #实例化
ins_1.var = 'hahaha'
ins_1.my_func()

ins_2 = MyClass()
ins_2.var = 'heihei'
ins_2.my_func()

#类的初始化和析构
#实例化时即添加实例属性
import time
class Food(object):
    def __init__(self,name):    #初始化实例
        self.name = name    #传入参数交给该实例属性保存；在多方法中通用
        print('食物的名字是：{}'.format(self.name))

    def __del__(self):      #实例销毁时执行
        print('{}被吃掉'.format(self.name))



    # def eat(self):
    #     print('{}正在吃饭'.format(self.name))
    #
    # def teach(self):
    #     print('{}正在上课'.format(self.name))


nanbei = Food('小鱼干')   #实例化时即自动执行

for i in range(10):
    print(i)
    if i == 3:
        del nanbei   #变量释放-即实例销毁
    time.sleep(1)

# for i in range(100):
#     print(i)
#     if i == 5:
#         nanbei = '南北'   #变量释放-即实例销毁
#     time.sleep(1)
