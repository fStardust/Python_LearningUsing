# BFS
# breadth-first search
# 广度优先搜索——查找两者间最少步骤
# Code python2.7 is from Aditya Bhargava's <Grokking Algorithms>
# Code python3.8 is here

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
