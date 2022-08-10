a = [int(i) for i in input().split()]
ones = []
more_one = []
for i in range(len(a)):
    count = 1
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1 and a[i] not in more_one:
        ones.append(a[i])
    else:
        more_one.append(a[i])

print(" ".join(str(i) for i in ones))
