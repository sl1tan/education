count = 0
x = -1
id = 0
prev = 0
while x != 0:
    x = int(input())
    if prev < x and id != 0:
        count += 1
    prev = x
    id += 1
print(count)
