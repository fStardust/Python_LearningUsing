"""
python·lesson5
散列类型、运算符优先级和逻辑运算
-集合
-字典
-逻辑运算符
-运算符优先级
"""
# 集合
my_list = [1,1,1,1,2] #集合无序
a = set(my_list) # 集合类型会自动删去重复
b = list(a) # 转换成列表
print(a)
print(type(a))
print(b)
print(type(b)) # 去重输出
a  = {}
print(type(a))

s1 = {1,2,3,4,5}
s2 = {4,5,6}
s3 = {2,3}
# isdisjoint issubset issuperset
print(s1 & s2) # 交集
print(s1 | s2) # 并集
print(s1 - s2) # 差集

s1.add('er') #末尾增值
print(s1)
print(s1.pop()) # 随机取出并删除一个值
print(s1)
s1.remove(3) # 指定删除
print(s1)
s1.update((9,10,12)) # 更新集合,叠加……
print(s1)
print(s1.isdisjoint(s2)) # 是否无交集
print(s1.issubset(s2)) # s1是否为s2子集
print(s1.issuperset(s1)) # s1是否为s2父集

# 字典——给每个值取名（键值对）键有唯一性，若同一字典有两个键，输出时随机保留一个
# 字典可变，键名不可变，键值可变——类型（键名不能用列表这类可变类型，常用字符串）
# 3.6版本之后有序——影响不大
my_dict = {
    'name':'王',
    'age':18,
    'height':180,
}
my_dict2 = dict(name = '改', age = '16', hight = 180)
my_list = [1,1,2,my_dict2] # 列表可以加任何东西
print(my_dict['age'])
print(my_dict2['age'])
my_dict['age'] = 20
print(my_dict) # 若原先有该键则修改
my_dict['weight'] = 40
print(my_dict) # 若原先无该键则添加
print(my_list)

a = my_dict.copy() # 等同列表浅拷贝
print(a)
print(id(my_dict))
print(id(a))
a = dict.fromkeys(['name','age','height'],100) # 通过可迭代对象（随机列表）生成有默认值的字典
print(a)
my_list = ['a','b','c']
a = dict.fromkeys(my_list,1)
print(a)
a = dict.fromkeys(my_list) # 若不加默认值则默认为None
print(a)
a = dict.fromkeys(my_list,(1,2))
print(a)
a = my_dict.setdefault('name') # 查找该字典有无所查键，若有则输出；若无则输出None且添加键
print(a)
print(my_dict)
a = my_dict.setdefault('a')
print(a)
print(my_dict)
a = my_dict.setdefault('c',50) # 若无则输出None且添加完整；若有则输出原值并不修改
print(a)
print(my_dict)
a = my_dict.setdefault('a',50)
print(a)
print(my_dict)
my_dict2.clear() # 删除所有
print(my_dict2)
a = my_dict.pop('c') # 删除该键值对，并返回删除键值对的值
print(a)
print(my_dict)
a = my_dict.popitem() # 随机删除该键值对，并返回删除的键值对
print(a)
print(my_dict)

new_dict = {'wei':4,'name':6}
my_dict.update(new_dict) # 更新字典，若有重复键则随机选值
print(my_dict)
print(my_dict['name']) # 查找该值并随机
print(my_dict.get('name'))
print(my_dict.get('n')) # 该方法若物质则输出None
# print(my_dict['n']) # 该方法若无值则报错
print(my_dict.keys()) # 取出键值得到列表
print(my_dict.items()) # 取出键值对得到元组

# 逻辑运算符
print(my_dict)
print(isinstance(my_dict,dict)) # 判断是不是某对象
print(10>20) # 比较运算符：==（等于）；!=(不等于)；>;<;<=;>=;
a = 25
b = 10
c = 15
print(a > b or c > b) # and与 or或 not非
a = 10
b = 10.0
print(a == b)
print(a is b) # 判断id
a = 10
b = '10'
print(a == b)


#运算符优先级
# 身份运算符，is（判断id）;is not
c = [1,2,2.5]
b = a
print(id(a))
print(id(b))
print(a is b)
b = c.copy()
print(id(a))
print(id(b))
print(a is b)
# 成员运算符,值是否在，in; not in
a = ['a','b','c']
b = 'a'
print(b in a)

a = 0
a += 1 # 赋值运算符：=前加其他运算符（/-+*）
print(a)
b = 0
b = b + 1
print(b)

# 算术运算符》比较运算符》赋值运算符》身份运算符》成员运算符》逻辑运算符
# 不推荐以上方法
# 推荐以加（）形式，优先级