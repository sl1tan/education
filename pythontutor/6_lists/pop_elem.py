a = input().split()
id = int(input())
for i in range(id, len(a) - 1):
    a[i], a[i + 1] = a[i + 1], a[i]
a.pop()
print(" ".join(a))
