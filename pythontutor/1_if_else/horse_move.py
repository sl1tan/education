x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

modx = abs(x1 - x2)
mody = abs(y1 - y2)

if x2 == x1 or y2 == y1 or (modx <= 1 and mody <= 1):
    print("NO")
elif modx <= 2 and mody <= 2 and modx != mody:
    print("YES")
else:
    print("NO")
