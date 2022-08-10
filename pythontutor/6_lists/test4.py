s = "1 2 3"
a = s.split()
print(a)
for elem in a:
    elem = int(elem)
# for i in range(len(a)):
#     a[i] = int(a[i])
print(a)
b = [int(char) for char in input().split()]
print(b)

print(".".join(a))
print("#".join(str(i) for i in b))
