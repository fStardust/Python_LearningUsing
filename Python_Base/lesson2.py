"""
python·lesson2
序列类型的方法
"""
#其下，无特别说明，参数也即索引值
a_list = ["sda",123,"safdf"]
print(id(a_list))
b_list = ["happy",123,123]
c_list = a_list + b_list # 无缝拼接列表
a_list.extend(b_list) # 扩展a列表
print(c_list)
print(a_list)
print(id(a_list))
b_list.append("feas") # 在列表末尾添加元素
print(b_list)
b_list.insert(2,"frwds") # 在列表该索引值处添加该元素
print(b_list)
b_list.pop() # 无参，默认为-1，删除该列表最后一元素；有参数即删除改位。
print(b_list)
b_list.pop(1)
print(b_list) # 有参数即删除改位。
a_list.remove("sda") # 删除列表中该值，若无则报错,若同列表有多个该值，则删除左至右第一个。
print(a_list)
c_list.clear() # 清空该列表
print(c_list)
print(a_list)
a_list[1] = "dsafsdaa" # 修改原列表对应索引值处数据，若超限则报错
print(a_list)
print(a_list.index("happy")) # 查找该元素所在列表索引值
print(a_list.count(123)) # 统计该元素在列表中的数量

#元组因其无法更改性，所以其自身方法只有查询的两种：count；index。具体使用跟列表方法一致
#元组的修改，要先转换成列表，对列表修改好后，在转换成元组。
a_tuple = ("happy","you","me","she","she")
print(a_tuple)
print(a_tuple.count("she"))
a_tuple_list = list(a_tuple)
print(a_tuple_list)
a_tuple_list[4] = "he"
print(a_tuple_list)
a_tuple = tuple(a_tuple_list)
print(a_tuple)

#字符串相关增删改查功能较多，其中增后续介绍；未说明即跟列表同名方法一样
#查：count，find（如同count，但找不到返回-1），index（可查找组合字符起始位置）；(是否为全数或全字母)isdigit,isalpha；（是否以某字段开头或结尾）endswith,startswith；（所含字符中的字母是否皆为大写或小写）islower,isupper。返回值为布尔类型
#改：生成新串（字符中字母转大写或小写）upper，lower；（删除字符串开头与末尾空格）strip,lstrip,rstrip;capitalize（未介绍）；title（未介绍）；split(按规则分割字符串）
#删：replace,该方法同样适用于改。删除既是把替换的内容置空。第三个参数若原串有多同值，改几次，默认-1即全改。
#转义字符:\。\r回车，移到本行开头;\n换行；\b退格；\\输出\;\0代表空字符；r取消转义
a_str = "         Hello world ! This is a python test.          "
b_str = "23144445"
print(a_str)
print(b_str)
print(a_str.find("sd"))
print(a_str.find("This"))
print(a_str.index(" is"))
print(a_str.count("is"))
print(a_str.isalpha())
print(b_str.isdigit())
print(a_str.startswith("Hello"))
print(b_str.endswith("445"))
print(a_str.islower())
print(id(a_str))
print(a_str.upper()) # 注意其实际上生成的是新串
print(id(a_str.upper()))
print(a_str.lower())
print(a_str.strip())
print(a_str.lstrip()) # 只去左边空格
print(a_str.rstrip())
c_str = a_str.strip()
print(c_str.split(" ")) # 根据空格将a串分割
print(a_str.strip().split(" "))
print(a_str.replace("world","you",1))

#编解码
a = "1234ab!"
print(a.encode('UTF-8')) # 国际通用字符集
print(a.encode('GBK')) # 中国自有字符集
b = "你好呀！"
print(b.encode('UTF-8'))
print(b.encode('GBK'))
c = b.encode('UTF-8')
print(c)
d = c.decode('UTF-8') # 使用编码对应的规则解码，若不对应则报错
print(d)