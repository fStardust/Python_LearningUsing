"""
python·lesson14
迭代器，生成器、认识模块和包
-推导表达式
-迭代器和生成器
-模块 -c为模块；-i为引用
-包和包管理
"""
# 推导表达式

my_list = []

for i in range(1, 10):
    my_list.append(i)

print(my_list)

my_list = list(range(1, 10))

my_list = [i for i in range(1, 10) if 1 % 2 == 0]
# 推荐最多三目运算符
# 列表推导式；通过该语句生成列表（将i放入该列表中）
print(my_list)
my_dir = {i: j for i, j in enumerate(['a', 'b', 'c'])}
my_str = {'wdaad' if i % 2 == 0 else 'dsad' for i in range(1, 10)}
print(my_dir)
print(my_str)

# 迭代器和生成器
# for 迭代变量 in 可迭代对象
# 每一次循环都会自动让“迭代变量”指向“下一个元素”
my_list = [1,2]
print(dir(my_list)) #变量的方法输出中有"__iter__"即为可迭代对象
a = iter(my_list)   #生成迭代器
b = my_list.__iter__() #与上行代码等价
print(a)
print(type(a))  #输出<class 'list_iterator'>，
print(dir(a))       #迭代器相对可迭代对象除了"__iter__"还有"__next__"方法
print(next(a))
print(next(a))  #迭代运行——依次取出
# print(next(a))  #报出迭代停止错误   StopIteration

#for实现原理：先将可迭代对象方法包装成迭代器，在内部依次取指，直到无值，就跳出循环
#即，可迭代对象就能进行for
#可迭代器，只能运行一次
class MyIter(object):
    def __init__(self,li):
        self.li = li
        self._index = 0

    def __iter__(self): #生成迭代器
        return self #拥有iter与next方法，已经是迭代器，可以返回自身

    def __next__(self):
        if self._index < len(self.li):
            number = self.li[self._index]
            self._index += 1
            return number
        else:
            raise StopIteration

my_list = [1,1566,5.45,455,454]
a = MyIter(my_list)
for i in a:     #该函数即是在多次调用该函数print(next(a))|print(a.__next__())
    print(i)

# 生成器;特殊的迭代器
#对延迟操作提供了支持
a = (i for i in range(1,10))    #将‘列表推导式’外面的[]改成()即为生成器
print(a)                        #只保存了数据生成的方式（调用时才生成数据），占用内存较小，缺点运行速度较慢
print(type(a))

b = [i for i in range(1,10)]    #列表推导式
print(b)                        #写出规则后即运行，并放入内存
print(type(b))

def number():
    num = 0
    while num < 100:
        yield num   #生成生成器，yield（暂停一个函数并返回出去）
        num  += 1

a = number()
for i in a:
    print(i)

# 模块，一个.py文件即被称为模块（一个功能一个模块）
def hello():
    print('hello leeson')

#在同一目录下，可以用以上方法导入（无需路径地址）
#不同路径下，需用相对地址或绝对地址导入(sys.path);导入后会在当前路径下生成一个__pycache__文件夹

# 包和包管理：包：多个模块放在一个文件夹；包管理：为方便该文件夹引用
# 包下必须得有__init__.py，才能做包管理。（可以无内容但必须得有）有该文件即被视作包文件
# 包文件不能作为顶级模块（即内部无主函数）
#代码位于frist包中
