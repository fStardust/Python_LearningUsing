"""
python·lesson8
函数作用域和匿名函数
-匿名函数
-函数作用域
-闭包
-递归和回调
"""

#匿名函数
#语法规则 lambda x:表达式
my_list = [101,15,151531,15]
result = filter(lambda x: True if x > 100 else False, my_list)
print(list(result))
#只能写一行……
a = lambda x: True if x > 100 else False
#可以给其命名

#函数作用域
#函数外部无法访问函数内部参数
#函数内部可以访问函数外部参数·全局变量，全大写
G = 100
def func():
    G = 50
    print(G)
func()  #先打印同名内部参数（由里到外依次搜索）
def func():
    G = 50
    print('函数内部G值：{}'.format(G))
func()
print('函数外部G值：{}'.format(G))
def func():
    global G #声明所用的是全局变量
    G = 50
    print('函数内部G值：{}'.format(G))
func()
print('函数外部G值：{}'.format(G))    #声明后可以更改全局变量
def func_out():
    mid_data = 'xxx'
    def func_in():
        nonlocal mid_data   #取得上一层变量
        print('打印：{}'.format(mid_data))
    func_in()
func_out()

#闭包
#调用函数内部函数
def func_out():
    a = 10
    return a
print(func_out())

def func_out(): #函数也是对象也能被传递，内部函数也是
    def func_in():
        print('我是里程函数。')
    return func_in()

result = func_out()
print(result)
result

def func_out(times):
    def func_in(num):
        return times * num
    return func_in

times_5 = func_out(5)
print(times_5(100))
#动态创建函数
#函数内部和函数外部沟通的桥梁

#递归和回调

# def func():
#     print('函数正在运行')
#     func()
#
# func()
#栈资源不够后报错

def factrial(num):  #阶乘实例
    if num == 1:    #退出规则
        return num
    return factrial(num-1) * num

print(factrial(3))
#代码虽然简洁，但规则不够清晰；占用内存较多

def add(x,y):
    return x + y
def multipy(x,y):
    return x * y
def use(func,num1,num2):
    return func(num1,num2)
a = 10
b = 15
print(use(add,a,b))
#自身是一个函数，只是被传入到其他函数供其调用；是否调用由内部逻辑决定

a = lambda  x : True if x > 10 else False
b = lambda  x : True if x < 10 else False
my_list = [10,20,30]
filter(a,my_list)
#由a，b决定使用哪种方法来处理数据

