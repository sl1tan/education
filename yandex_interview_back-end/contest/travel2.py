import collections


def calculate_distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])


def all_possible(point):
    all = set()
    for city in cities:
        if calculate_distance(cities[point], cities[city]) <= length:
            all.add(city)
    return all


def bfs(graph, start, end):
    level = [-1] * (len(graph) + 1)
    level[start] = 0
    visited, queue = set(), collections.deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                level[neighbour] = level[vertex] + 1
                if neighbour == end:
                    return level[neighbour]
                queue.append(neighbour)
    return -1


n = int(input())
cities = {}
for num in range(1, n + 1):
    x, y = [int(i) for i in input().split()]
    cities[num] = [x, y]
length = int(input())
start, end = [int(i) for i in input().split()]

graph = dict()
for city in cities:
    graph[city] = all_possible(city)

# Driver Code
if start == end:
    print(0)
elif calculate_distance(cities[start], cities[end]) <= length:
    print(1)
else:
    print(bfs(graph, start, end))
