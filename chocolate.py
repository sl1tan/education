n = int(input())
m = int(input())
k = int(input())

S = n * m
if k > S:
    print("NO")
elif k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")