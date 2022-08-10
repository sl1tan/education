x = -1
count = 1
id = 0
while x != 0:
    x = int(input())
    if x != 0:
        if id == 0:
            prev = x
            id += 1
        if prev == x:
            if id > 1:
                count += 1
            id += 1
            if count == 1:
                max = count
            if max < count:
                max = count
        else:
            prev = x
            count = 1
            id += 1
print(max)
