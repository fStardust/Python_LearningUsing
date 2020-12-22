def hello():
    print('hello leeson')

def ChromWebDriver():
    print('hihi')

print(__name__)     #若有此模块，则导入后输出包含该函数的主函数

if __name__ == '__main__':  #只有在运行当前该模块是才会执行；控制代码在被其他模块导入时不主动执行
    print('我是主函数')          ##也即：如果模块是直接运行的，则代码块会被直接运行，如果模块是被导入的，则代码块不被运行