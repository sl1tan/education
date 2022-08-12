a = []
for i in range(5):
    a.append(input())
for i in range(len(a) - 1, -1, -1):
    if len(a[i]) == 0:
        a.pop(i)
print(a)
