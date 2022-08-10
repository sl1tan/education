a = [int(i) for i in input().split()]
id, num = [int(i) for i in (input().split())]
a.append(num)
for i in range(len(a) - 1, id, -1):
    a[i] = a[i - 1]
a[id] = num
print(" ".join(str(i) for i in a))
