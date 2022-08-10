x = -1
max = 0
count = 0
while x != 0:
    x = int(input())
    if x > max:
        max, count = x, 1
    elif x == max:
        count += 1
print(count)
