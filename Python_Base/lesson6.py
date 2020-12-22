"""
python·lesson6
控制流程
-条件判断
-三目运算
-while循环·判断循环
-for循环·迭代循环
"""
# 条件判断
my_num = 100
if my_num >100:
    print('数字大于100')
    print('很不错')
else:
    print('数字不大于100')
    print('很不好  ')

my_num = 0
if my_num >100:
    print('数字大于100')
    print('很不错')
elif my_num ==  0 or my_num ==10:
    print('数字等于0')
else:
    print('很不好  ')

# 三目运算符
a = 10
print(True) if a > 5 else print(False)
a =1 if a > 5 else 2
print(a)

# while循环·选择循环
if a > 5:
    print(True)
else:
    print(False)
a = [15,1,2,7,69]
i = 0

while i < len(a): # else只有在while不被break中途跳出时才执行
    if a[i] > 5:
        print(True)
    else:
        print(False)

    if a[i] == 9:
        print("值为7，跳出循环")
        break

    i += 1

else:
    print('循环结束跳出')

#for 循环·迭代循环
a = [15,1,2,7,69]
i = 0
while i < len(a):
    if a[i] > 5:
        print(True)
    else:
        print(False)
    i += 1

for i in a:
    if i > 5:
        print(True)
    else:
        print(False)

for i in a:
    print(i)

a = list(range(0,100,5))
print(a)
print(range(20))
for i in range(0,50):
    print(i)

for i in range(1,21): # 使用continue跳过本次循环
    if i % 5 == 0:
        continue
    print(i)
else:
    print('ho')

# import time
# while True:
#     print('3')
#     time.sleep(1)

print('h',end='')
print('d')

#Linux 命令
# cal 查看当前日期； -y输出全年
#     October 2020
# Su Mo Tu We Th Fr Sa
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
# date 查看现在时间
# Fri Oct  9 20:05:11 CST 2020
# sl 跑个火车

