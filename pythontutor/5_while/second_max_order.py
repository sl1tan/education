x = -1
id = 0
while x != 0:
    x = int(input())
    if id == 0:
        max = int(input())
        prev_max = x
        if max < prev_max:
            max, prev_max = prev_max, max
            x = prev_max
        id += 1
    if x != 0 and id > 0:
        if max < x:
            prev_max = max
            max = x
        elif prev_max < x:
            prev_max = x
        id += 1
print(prev_max)
