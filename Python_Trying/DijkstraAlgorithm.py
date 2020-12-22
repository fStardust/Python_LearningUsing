# DijkstraAlgorithm
# 狄科斯特拉算法·深度优先算法
# 主要特点是从起始点开始，采用贪心算法的策略，
# 每次遍历到始点距离最近且未访问过的顶点的邻接节点，
# 直到扩展到终点为止/或者达到目标位置。

# graph：第一个散列表，用于存储各直连节点及其开销
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}  # 终点没有任何邻居

# costs:第二个散列表，创建开销表，并定义初始无穷开销数值
infinity = float("inf")  # 初始时不知道开销时，设置成无穷大
costs = {}  # 具体开销，实时更新
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents:第三个散列表，储存父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = []  # 记录处理过的节点


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # 若当前节点开销更低且未处理
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 找出接下来要处理的点，并循环
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# 输出开销最小
print(costs)
"""
    输出结果及解释：
    输出：{'a': 5, 'b': 2, 'fin': 6}
    起点到a节点的开销最小为：5
    起点到b节点的开销最小为：2
    起点到fin节点（终点）的开销最小为：6
"""
