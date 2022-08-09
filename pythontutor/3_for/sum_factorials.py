n = int(input())
res = 1
sum = 0
for i in range(1, n + 1):
    res *= i
    sum += res
print(sum)
