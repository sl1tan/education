a = [1, 2, 3]
print(a)
for i in range(len(a)):
    print(a[i])
for elem in a:
    if elem != a[len(a) - 1]:
        print(elem, end=" ")
    else:
        print(elem)
print(a[::-1])
for i in range(len(a) - 1, -1, -1):
    if i != 0:
        print(a[i], end=" ")
    else:
        print(a[i])
b = a[::-1]
for elem in b:
    if elem != b[len(b) - 1]:
        print(elem, end=" ")
    else:
        print(elem)
for elem in reversed(a):
    if elem != a[0]:
        print(elem, end=" ")
    else:
        print(elem)
c = str(b)
print(c)
