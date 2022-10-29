n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([str(j) for j in input()])
print("-------------------------------------------------------")


def mirror(seq):
    output = list(seq[::-1])
    output.extend(seq[1:])
    return output


b = a[::-1]
c = b[1:]


for i in range(0, len(b)):
    for i2 in range(0, len(b[i])):
        print(b[i][i2], end='')
    print()

print("--------------------------------------------")

for i in range(0, len(c)):
    for i2 in range(0, len(c[i])):
        print(c[i][i2], end='')
    print()

print("--------------------------------------------")

for i in range(0, len(a)):
    for i2 in range(0, len(a[i])):
        print(a[i][i2], end='')
    print()
