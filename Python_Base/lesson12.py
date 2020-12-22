"""
python·lesson12
文件
-文件操作
-IO流
-上下文管理
-OS模块
"""
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
def type1():
    for i in range(1000000):  # 重复运行减少误差
        type(1)


@run_time
def isinstance1():
    for i in range(1000000):
        isinstance(1, int)


type1()  # Linux上的时间戳更为精准；Windows可能输出0
isinstance1()  # Linux上的时间戳更为精准；Windows可能输出0

print(time.time())
# 获得Unix时间戳（Unix Timestamp），Unix于1970年投入使用
# Unix时间戳：格林威治时间自1970年1月1日（00:00:00 GMT）至当前时间的总秒数
# 时间戳：唯一的标识某一刻的时间


# 文件操作
# 参数：
# r:只读取，不存在则报错
# w：若不存在则创建写入；若存在则覆盖
# a：追加,不存在则创建
# r+/w+/a+：读写，文件指针（光标）默认分别在开头（报错）/覆盖（创建）-打开一个文件的时候，默认清空/结尾（创建）——文件是否存在
# rb/rb+/wb/wb+/ab/ab+;加个b的作用：以二进制形式完成以上操作

# f = open('haha.txt','w')    #相对目录，在当前目录下寻找，若无则创建文件
# f.write('heihei')           #写入
# f.close()                   #关闭

f = open('/home/pyvip/python/lesson/1.txt', 'a+')
# print(f.read()) #读取完整文件，带参输出固定字符串长数的内容（从游标开始读到文档末尾）
print(f.tell())  # 输出光标位置——距离开头？字长
f.seek(5)  # 移动光标，负←；正→；注意a+是追加字符不能随意改变光标位置；所以可以用r+
print(f.tell())
# print(f.readline()) #读取一行
# print(f.readline(4)) #读取一行，带参输出固定行
# print(f.readlines())#读取所有行并作为列表元素输出，带参输出固定行数
f.write('''gduaji
        dasdadaddd
        'sadad' ''')
f.writelines('\n hahah \n')  # 输入一行，要输入换行符，不然默认在结尾后写入
f.close()

# f = open('/home/pyvip/python/lesson/1.txt','a+')
# f.write('1111')
# f.close()     #在行命令模式下，需要关闭（保存）才能完整输出；不然只运行但不保存；也可以用f.flush()刷新缓存，写入文件
# f = open('/home/pyvip/python/lesson/1.txt','a+')
# f.flush()     #刷新缓存，写入文件

# IO流：内存假文件（为了运行效率）模式——文本模式；二进制模式；关闭后即不存在（f.close等效）

import io

f = io.StringIO()  # 文件模式
f.write('10000')
f.seek(0)  # 需要将光标置于开头
print(f.read())  # 从游标开始读到文档末尾
f = io.BytesIO()  # 二进制模式
f.write(b'100a0')
print(f.getvalue())  # 获取所有内容

# 上下文管理:前后环境操作
with open('lesson11.py', 'r') as f, \
        open('lesson10.py', 'r') as m:  # 通过该方法让python自动关闭（不用写close()关闭保存）；也可如此多文件操作
    print(f.read())  # 代码太长可以用\转接（不常用）
    print(m.read())

with open('/home/pyvip/python/lesson/1.txt', 'a+', encoding='utf8', errors='ignore') as f:
    f.write('南北')  # 此时输入的仍然是utf—8格式，gbk不认识|encode（'gbk'）使用gbk输出
# encoding='gbk'指定格式；errors='ignore'忽视报错；errors='static'较严格格式时报错（讲的有些不清）
# 注意不同平台的编码格式（显示，远程等……）

# OS模块
import os

print(os.getcwd())  # 显示当前路径
# print(os.listdir())    #展示当前目录内容
# os.chdir()      #改变当前路径
# os.mkdir()      #创建目录
# os.rmdir()      #删除目录
print(os.system('ls'))  # 使用Linux命令,有一些会错（比如：火车-sl）
# os.remove()     #删除文件
# os.rename()     #重命名

print(os.path.join('/home/p', 'p/j', 'ho'))  # 拼接多个目录，以后数'/为开头截止，每段自动拼接前加/

# os中有多种方法，要用的时候再查即可
