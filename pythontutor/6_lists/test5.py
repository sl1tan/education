a = list(input())
print(a)
print(a[2:4])
temp = a[-1]
a[-1] = a[0]
a[0] = temp
print(a)
a.sort(reverse=True)
print(a)
a[0], a[-1] = a[-1], a[0]
print(a)
a.sort(reverse=True)
print(a[::-2])
