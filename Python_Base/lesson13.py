"""
python·lesson13
异常
-异常
-处理异常
-断言
"""
#异常
'''
代码错误
#错误提示且错误位置指定错误（语法错误）
#报错位置错误（语法错误）
#根本没有错误信息——输出与预想不对（逻辑错误）
    异常本身是个类（语法异常）如下举例
    所有异常都继承自BaseException可大致分如下四类
        SystemExit退出异常
        KeyboardInterrupt键盘打断（Ctrl+C)-主动打断
        GeneratorExit生成器异常
        Exception普通异常（大多数）
    异常回溯：异常会输出完整的错误代码运行路径
如何提问：
    代码完整截图
    错误表征
    自我思考缘由
'''
# help(NameError)

#处理异常
for i in range(10):
    try:                #将自己认为有错的代码放入try之下
        print(i)
        if i == 5:
            print(hello)
    except Exception as e:   #不带关键字则任何错误都被捕捉；捕捉该类包含的错误，若有则执行下面的语句；若错误不包含于此则正常报错。
        print(e)             #通过e变量输出错误信息
    except NameError as f:   #可写多个
        print(f)
    except (TabError,NameError) as g:   #可一起判断
        print(g)
        # continue        #跳过该循环
    else:   #try下无错则执行else下面的代码
        print('lal')
    finally:    #有错也运行，代表整个程序块的运行
        print('有错也运行')

#自定义异常
# class MyError(Exception):   #自定义了一个MyError错误类型（继承自Exception）
#     pass
#
# a = 'xxx'
# b = 'cac'
#
# if a == 'xxx':              #自定义报错逻辑
#     raise MyError("由于a的是'xxx'所以报错")           #返回报错格式，（）内为报错说明

# 断言
a = 5
assert a == 5,'变量{}错误'.format('a')   #强制a等于5，验证a变量的格式，若不满足则报错。内部返回TF；在程序运行中加一道关口——自我检查的过程。

print(a + 77)

f = open('lesson1.py','r')

try:
    content = f.read()
    print(conten)
except NameError as e:
    print('变量错误{}'.format((e)))
finally:    #哪怕错误也正常关闭；强制运行
    f.close()
    print("文件正常关闭了")

def h():
    try:
        return 10   #原先这里便输出与关闭，但finally强制执行，用新的return顶掉了这个10
    except Exception as e:
        return 20
    else:
        return 30
    finally:
        return 40
