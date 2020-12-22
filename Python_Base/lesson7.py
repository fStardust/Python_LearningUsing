"""
python·lesson7
函数基础和函数参赛
-函数基础
-函数参数
-python常见内置函数
"""

# 函数基础

g = 5

def say_hello():
    print('hello world')


say_hello()
def say():
    for j in range(1, 10):
        for i in range(1, j + 1):   # 输出限制
            print('{}*{}={:<2}'.format(i,j,i * j),end=' ') # 同行输出
        print() # 换行
    pass # 结束

say()


def say():
    a = 10
    a = a * g
    return a

print(say())

g = 10
def say_h():
    say_b()
def say_b():
    print(g)
say_h()

# 函数参数
a = 10
b = 20

def say_h(arg_1,arg_2=1000): # 默认参数要放在后面
    a = arg_1 + arg_2
    return a

print(say_h(a))
print(say_h(a,b)) # 传特定值即不用默认值

def say_h(*args): # 不定参数
    return args

print(say_h(10)) # 传不定长参数传值，包装成元组

def say_h(**kwargs): # 传关键字参数传值，包装成元组
    return kwargs

print(say_h(name='hello ',lesson='python'))

def say_h(name,action,*args):
    result = name + ' ' + action + ' '.join(args)
    return result
print(say_h('dai','学习','henhao','很棒'))

def say_h(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)
say_h(1,12,23,'dai','学习','henhao','很棒',hoijad = 'adjia',asd = 'dsa')

def say_h(arg):
    print(arg)
    print(type(arg))
say_h([1,23,4])

def m_1():
    print('函数')
def say_h(arg):
    print(arg)
    print(type(arg))
say_h(m_1) # 传入为函数本身
say_h(m_1()) # 传入为函数输出

# 默认参数要位于必备参数后面
def f(a,b,c):
    print(a)
    print(b)
    print(c)
my_list = [12,231,2313]
my_c = {'a':10,'b':'asd','c':'asda'}
f(*my_list) # 解开列表接替传值
f(**my_c) # 元组解包

# 常见内置函数
print("------------------------------")
for i in dir(__builtins__): # 内置对象查看
    print(i)
print("------------------------------")
# len 求长度
# min 求最小值；max 求最大值
# sorted() 排序；reversed=Ture反向
# reversed() 反向
# sum() 求和
# bin() 转二进制
# oct() 转八进制
# hex() 转十六进制
# ord() 字符转ASCII码
# chr() ASCII码转字符


enumerate # 返回可枚举对象
a = [56,67,1,6100,565]
print(dict(enumerate(a)))
for i in enumerate(a):
    print(i)
for a,b in enumerate(a):
    print(a)
    print(b)

a = eval('16 + 15') # 取出字符串内容并运行
print(a)
a = eval('print("ashdikjda")')
print(a)

def fun():
    print('i am fu')
a = exec('fun()') # 该函数本身不输出结果
print(a)

a = [1,2,3]
b = ['a', 'b', 'c']
print(list(zip(a,b))) # 匹配输出
for i,j in zip(a,b):
    print(i * j)

a = [1, 2, 3]
def f(args):
    return args * 100
r = list(map(f,a)) # 重复应用函数
print(r)

a = [1, 8, 2, 3, 4, 5, 6]
def f(args):
    if args > 2:
        return True
    else:
        return False
r = list(filter(f,a)) # 该函数必须要返回对错；做筛选
print(r)

# Linux命令
# alias命令别名，暂时性的：
# alias cy='cd py_case' -sy 指替代函数名，''内为原函数名
# unalias取消别名
# unalias cy