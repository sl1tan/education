def level(graph, child, zero_parent):
    lvl = 1
    if child == zero_parent:
        return 0
    parent = graph.get(child, zero_parent)
    if parent == zero_parent:
        return lvl
    return level(graph, parent, zero_parent) + 1

def check(parent, child):
    if graph[child] == parent:
        return 1
    elif level(graph, parent, zero_parent) == level(graph, child, zero_parent):
        return 0
    return check(parent, graph[child])


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

for n in range(int(input())):
    ch1, ch2 = input().split()
    lvl1 = level(graph, ch1, zero_parent)
    lvl2 = level(graph, ch2, zero_parent)
    if lvl1 == lvl2:
        print(0, end=" ")
    elif lvl1 < lvl2:
        if check(ch1, ch2):
            print(1, end=" ")
        else:
            print(0, end=" ")
    else:
        if check(ch2, ch1):
            print(2, end=" ")
        else:
            print(0, end=" ")
