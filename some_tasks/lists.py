
a = [int(i) for i in input().split()]
try:
    id = a.index(20)
    a[id] = 200
    print(a)
except:
    print(a)
