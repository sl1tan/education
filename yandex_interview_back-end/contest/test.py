from itertools import combinations

input = ["(", ")"]

output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])