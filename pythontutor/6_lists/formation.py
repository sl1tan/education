a = [int(i) for i in input().split()]
height = int(input())
count = 1
for elem in a:
    if elem >= height:
        count += 1
print(count)
