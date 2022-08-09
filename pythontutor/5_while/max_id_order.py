x = -1
id = 0
x = int(input())
max = x
max_id = id
while x != 0:
    x = int(input())
    id += 1
    if x > max:
        max = x
        max_id = id
print(max_id)
