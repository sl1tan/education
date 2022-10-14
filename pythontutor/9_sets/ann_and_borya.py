a = set()
b = set()

count_a, count_b = [int(i) for i in input().split()]
for x in range(count_a):
    a.add(int(input()))
for x in range(count_b):
    b.add(int(input()))

inter = a & b
len_inter = len(inter)

dif_a = a.difference(b)
len_dif_a = len(dif_a)
dif_b = b.difference(a)
len_dif_b = len(dif_b)

print(len_inter)
print(*sorted(inter))
print(len_dif_a)
print(*sorted(dif_a))
print(len_dif_b)
print(*sorted(dif_b))