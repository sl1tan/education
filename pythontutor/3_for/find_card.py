n = int(input())
allCard = 0
for i in range(1, n + 1):
    allCard += i

for i in range(n - 1):
    allCard -= int(input())

print(allCard)
