"""
python·lesson1
数据类型和序列类型
"""
# python是解释型语言！
# 导入数学模块
import math
# 导入精确数值模块
from decimal import Decimal

print(10)
print(10 / 3)
a = 10
b = 3
c = a / b
print(type(a))
print(type(c))
print(c)
c = int(c)
print(type(c))
print(c)

# 注意：若要精确(导入decimal模块)浮点数，要加引号；整型不用
# 未讲理解：浮点数原本精确便在小数点后，整型原本精确至小数点；整型进行运算，自然下降一级至浮点数
print(Decimal(10) / Decimal(3))
# 使用math模块，计算π/2的sin值
d = math.sin(math.pi / 2)
print(d)

e = "Hello world!'你好'"  # 字符串，三种引号都可，但前后引号要保持一致，嵌套引号要注意不能重复
print(e)
# 列表可增修、元组不行。可嵌套，可转换。
# 切片规则对两者都适用。[a,b,c]a起始点，b终止点，c步长。
# 注意终止点为开区间。若要从开头取到结尾规范为：[0:];若后值超过范围，不报错，取全部。
f = (1, 1.2, "Hello", True)  # 元组
g = [1, 1.2, "Hello", True]  # 列表
h = "20190806"
print(f)
print(g)
print(f[-2])
print(g[2])
print(g[2:3][0])  # 列表切片后仍然还是列表可以直接索引取值
print(h)
print("年为:h[0:4],月为:h[4:6]日为:[6:]")
print(h[0:4])
# 潭州所布置作业如上——完成
