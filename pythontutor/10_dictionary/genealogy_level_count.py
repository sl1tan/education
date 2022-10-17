def level(graph, child, zero_parent):
    lvl = 1
    parent = graph[child]
    if parent == zero_parent:
        return lvl
    return level(graph, parent, zero_parent) + 1

n = int(input())
graph = {}
for x in range(n - 1):
    child, parent = input().split()
    graph[child] = parent

tree = {}
for child in graph:
    if graph[child] not in graph.keys():
        zero_parent = graph[child]
        tree[zero_parent] = 0

for key in graph:
    tree[key] = level(graph, key, zero_parent)

for key in sorted(tree):
    print(key, tree[key])