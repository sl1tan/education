a = [int(i) for i in input().split()]
for i in range(len(a)):
    a[i] **= 2
print(" ".join(str(i) for i in a))
