u = int(input())
hours = int(input())
len = 109
if u < 0:
    u = len + u
point = (u * hours) % len
print(point)
