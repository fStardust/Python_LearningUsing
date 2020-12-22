"""
python·lesson4
格式化输出、字符串拼接和深浅复制
-拼接
-复制
-二进制序列类型
-Linux用户
"""

# 字符串拼接·重点
a = "%s, hello ,  i am %s" # %用于占位
b = "lin"
c = "qi"
print(a  %(b , c) ) # 控制前后位置
my_list = ["hello","world","prython"]
a = '==='.join(my_list) # join方法前的参数是列表拼接之间的间隔符
print(a)
# 用{}代替%s
a = 'HEllo,{name},today is {date}'
print(a.format(name='lin',date='6号')) # 增加代码可阅读性
# %s字符（宽容）；%d整型（输入小数省去后面） ；%f浮点数（字符报错）
# %cASCII字符；%o8进制；%x16进制；%e科学急速发
# %+f,显示正数；%-n.mf，左位不够向左对齐,m表示小数位，n表示整数位
str_a = "today is %-0.4f"
print(str_a %3.66)
# %ns 参数n表示向字符末尾右对齐并格式化字符长度,添"-"则相反
str_a = "today is %15s"
print(str_a %"hello")
print(str_a %"Process")
print(str_a %"Hi")
str_a = "today is %-15s you are bard"
print(str_a %"hello")
print(str_a %"Process")
print(str_a %"Hi")
a = 'Hello, {:.5f},today is {b:.2f}' # 类似%nm、f
print(a.format(55.88, b=5.959959))
a = 'Hello, {:x},today is {b:o}' # 将输入转换成16进制——x，将输入转换成8进制
print(a.format(29, b=29))
a = 'Hello, {:<10},today is {b:2<5}' # 补齐字符长度，不足处用2来补齐（：2<5）——左对齐（>右对齐）
print(a.format(10, b=10))
a = 'Hello, {:^10},today is {b:2^5}' # 补齐字符长度，不足处用2来补齐（：2<5）————中间对齐
print(a.format(10, b=10))
a = 'Hello, {{tim，Harry}},today is {}'.format('bay bay') # 叠加{}来取消转义
print(a)
name = 'tidi'
date = '18'
print('hello, {}, today is {}'.format(name,date))
# print(f'hello, {name}, today is {date}' 更高版本使用，python>3.6
print('{:.3%}'.format(0.32)) # 将输入装换成%格式，参数表示小数位数

# 复制
a = [1,2,3,4]
b = a.copy()
a[0] = 100
print(a)
print(b)    # 浅复制
a = [1,2,[10,20]]
b = a.copy()
a[2][0]= 100
print(a)
print(b)    # 并非浅复制……
print(id(a))
print(id(b))
print(id(a[2]))
print(id(b[2]))
# copy并没有完全复制原列表值
import  copy
a = [1,2,[10,20]]
b = copy.deepcopy(a) # 深拷贝——多层嵌套需要使用
a[2][0]= 100
print(a)
print(b)
print(id(a))
print(id(b))
print(id(a[2]))
print(id(b[2])) # 内外层id不同

# bytes 二进制序列类型
a = b'hello world' # 这只能用于全ASCII表达
print(a)
print(type(a))
a = 'hello world.黄中' # 常规转换——输出结果转换为16进制
b = a.encode()
c = a.encode('gbk')
print(b)
print(c)
print(type(b))
#bytearray 二进制数组
a = b'hello world'
b = bytearray(a)
print(b)
print(type(b)) # 二进制字符对象
print(bytearray(3)) # 指定长度的零填充字节对象

# Linux用户
# cat /etc/passwd
# pyvip:x:1000:1000:pyvip,,,:/home/pyvip:/bin/bash #用户名；密码（不可见x）；；注释；用户主目录
# 超级用户——root
# 系统用户——系统正常使用的账户（不能登陆）
# 普通用户——特定权限受到控制
# cat /etc/group
# 用户组——按用户组分配权限