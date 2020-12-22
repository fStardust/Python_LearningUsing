"""
python·lesson15
正则
-正则表达式
-re模块
-元字符
"""
# 正则表达式
# 判断字符串是否匹配给定的格式
# 抓取页面的链接
# 判断数据格式
# 抓取页面特定数据

# re模块
# 集成了python中几乎所有有关正则表达式

import re

my_str = 'dgasuidihakdjslijdilajiduiqw哈斯低价地大多阿基多里阿杰大多啊点击率的加'
result = re.findall('大多', my_str)  # 查找多个结果
print(result)
result = re.match('dg', my_str)  # 自左索引，索引不到及报错。只查找一个
print(result)
print(result.span())
result = re.search('大多', my_str)
print(result)
print(result.span())

# 元字符
'''
单字符匹配
.   匹配任意一个字符（除了\n）
[]  匹配[]中列举的字符
\d  匹配数字
\D  匹配非数字
\s  匹配空白
\S  匹配非空白
\w  匹配单词字符，及a-z；A-Z;0-9;_
\W  匹配非单词字符
'''
my_str = '''哈斯 低价
    地大多阿基
         w哈斯低价地大多阿基多
         里阿杰大多啊点击率的加'''
result = re.search('......', my_str)  # 空格也算字符哦；
print(result)
print(result.group())
result = re.search('......', my_str, re.S)  # 忽视换行符
print(result)
print(result.group())

my_str = '回复‘a’回复‘b’回复‘c’das'
result = re.findall('回复‘[ab]’', my_str)  # 设定条件，只匹配单个数字
print(result)

'''
代表数量的元字符
*   匹配前一个字符出现0次或无限次
+   匹配前一个字符出现1次或无限次
?   匹配前一个字符出现1次或0次
{m}     匹配前一个字符出现m次
{m,}    匹配前一个字符至少出现m次
{m,n}   匹配前一个字符出现m到n次
'''
my_str = '回复‘7342890’回复‘23168’回复‘37’das'
result = re.findall('回复‘\d{3,}’', my_str)
print(result)

'''
代表边界的元字符
^   匹配字符串开头
$   匹配字符串结尾
\b  匹配一个单词的边界
\B  匹配非单词边界
'''
my_str = 'helloword hello ih akdjslijdi lajiduiqw'
result = re.findall(r'hello\b', my_str)  # 取消转义
print(result)

# 分组匹配
my_str = 'helloworld hello ih akdjslijdi lajiduiqw'
result = re.findall('world|ih', my_str)  # 匹配左右两个表达式
print(result)

my_str = '回复‘7342890’回复‘23168’回复‘37’das'
result = re.findall('回复‘(\d*)’', my_str)  # 最终提取出来的只有()中的内容
print(result)
# 贪婪模式
# 非贪婪模式  用一般锚定界限时（eg:‘’）推荐在任意取值方式时增加?

my_str = '回复‘7342890’回复‘23168’回复‘37’das'
result = re.findall('回复‘(.*)’', my_str)
print(result)

my_str = '回复‘7342890’回复‘23168’回复‘37’das'
result = re.findall('回复‘(.*?)’', my_str)
print(result)
