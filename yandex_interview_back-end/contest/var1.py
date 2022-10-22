def calculate_distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

def all_possible(point):
    all = set()
    for city in cities:
        if city not in processed:
            if calculate_distance(cities[point], cities[city]) <= length:
                all.add(city)
    return all


def find_path(start, end, count=1):
    from_start = all_possible(start)
    from_end = all_possible(end)

    if from_start & from_end:
        return count + 1
    elif not from_start or not from_end:
        return -1
    else:
        for point in from_start:
            processed.add(point)
            if all_possible(point) & from_end:
                return count + 1
        for point in from_start:
            return find_path(point, end, count + 1)

n = int(input())
cities = {}
for num in range(1, n + 1):
    x, y = [int(i) for i in input().split()]
    cities[num] = [x, y]
length = int(input())
start, end = [int(i) for i in input().split()]

answer = set()
processed = {start, end}
if start == end:
    print(0)
elif calculate_distance(cities[start], cities[end]) <= length:
    print(1)
else:
    print(find_path(start, end))