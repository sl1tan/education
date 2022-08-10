a = [int(i) for i in input().split()]
list_twices = []
list_count = []
copy = a.copy()
twices = 0
for i in range(len(copy)):
    count = copy.count(copy[i])
    if count > 1 and copy[i] not in list_twices:
        list_twices.append(copy[i])
        list_count.append(count)
for elem in list_count:
    twices += (elem * (elem - 1)) // 2
print(twices)
