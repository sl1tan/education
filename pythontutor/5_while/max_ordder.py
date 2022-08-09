x = int(input())
max = x
while x != 0:
    max = x if max < x else max
    x = int(input())
print(max)
