a = int(input())
b = int(input())
n = int(input())

cost = n * (a * 100 + b)

print("{} {}".format(cost // 100, cost % 100))
