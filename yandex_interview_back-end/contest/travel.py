def calculate_distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])


n = int(input())
cities = {}
for num in range(1, n + 1):
    x, y = [int(i) for i in input().split()]
    cities[num] = [x, y]
length = int(input())
start, end = [int(i) for i in input().split()]
distance = {}
distance[start] = {}
distance[end] = {}
for city in cities:
    distance[start][city] = {city:calculate_distance(cities[city], cities[start])}
    distance[end][city] = {city:calculate_distance(cities[city], cities[end])}















print("------------------------------------------------------------------")
for key in distance:
    print(str(key)+": ")
    for elem in distance[key]:
        for town in distance[key][elem]:
            print(town, distance[key][elem][town])

# print(distance[start][].values())