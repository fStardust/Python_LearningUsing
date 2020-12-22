# 简略·广度优先搜索·BFS

breadth-first search

#### 代码展示

使用《算法图解》中的“经销商查找”案例

```python
from __future__ import print_function
```

使用python3.x的print()形式——python3.x并不向下兼容

```python
# BFS
# breadth-first search
# 广度优先搜索——查找两者间最少步骤
# Code python2.7 is from Aditya Bhargava's <Grokking Algorithms>
# Code python3.8 is here

"""
	将书中的2.7版本改为3.8版本
	并无多少区别
	注意：
	python3.x中 return只能用在 函数（def）中
	python3.x 不支持 print 语句，支持print()语句
	python2.6，python2.7 可以通过：
	from __future__ import print_function
	使用 Python3.x 的 print 函数
"""

"""用到散列表"""
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search_queue = deque()
search_queue += graph["you"]

"""判断某人是否为经销商"""
def person_is_seller(name):
    return name[-1] == 'm'


# """P87·循环确定朋友中符合条件的人"""
# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(person + " is a mango seller!")
#         break
#     else:
#         search_queue += graph[person]


"""P90·优化P87页代码·用函数封装以上功能，认证过的加入列表，防止死循环"""
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")

# Python3.x 与 Python2.x 的许多兼容性设计的功能可以通过 __future__ 这个包来导入
```

*散列表：等价字典——以某种条件映射在对应储存空间

因为映射，所以查找对应数据较快，无需按个比较。

#### 广度优先搜索

广度优先搜索算法的基本是算出两点间的最短路径数。

两点可以一个是出发点，一个目标点。

例如：

- 象棋中最少走多少步可以获胜；
- 根据人际关系网络查找跟你关系最近的医生；
- 计算最少编辑多少处可以将错误单词改正；
- ……





