"""
九九乘法表·多看看，多写，多想几种成功运行的例子。成功将昨天的问题想明白。
"""
for i in range(1, 10):
    for j in range(1, i + 1):  # 输出限制
        print('{}*{}={:<2}'.format(i, j, i * j), end=' ')  # 同行输出
    print()  # 换行

# n = range(1,10) # 跟上一种没有什么差别
# for i in n:
#     for j in range(1,i + 1):
#         print('{}*{}={:<2}'.format(i,j,i * j),end=' ')
#     print()


# 昨天第一个想到的方法，错误原因是忘记将整型转换为字符串，导致一直报错
# i = 0
# while i < 9:
#     i += 1
#     j = 1
#     while j < i + 1:
#         a = '%s*%s=%s'
#         print(a%(str(i),str(j),str(i*j)),end=' ') #***
#         j += 1
#     print()

# for i in range(9,0,-1):
#     for j in range(1,i+1):   # 输出限制
#         print('{}*{}={:<2}'.format(i,j,i * j),end=' ') # 同行输出
#     print() # 换行
#
# j = 0
# while j < 9:
#     j += 1
#     i = 1
#     while i < j + 1:
#         a = '%s*%s=%s'
#         print(a%(str(i),str(j),str(j*i)),end=' ') #***
#         i += 1
#     print()

# for j in range(1, 10):
#     for i in range(1, j + 1):   # 输出限制
#         print('{}*{}={:<2}'.format(i,j,i * j),end=' ') # 同行输出
#     print() # 换行
# 这个更加规整，可以更好控制结构的整齐。
