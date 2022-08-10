a = [int(i) for i in input().split()]
max_id, min_id = a.index(max(a)), a.index(min(a))
a[max_id], a[min_id] = a[min_id], a[max_id]
print(" ".join(str(i) for i in a))
