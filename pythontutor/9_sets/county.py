def count_days(n, start, sep):
    days = set()
    for x in range(start, n + 1, sep):
        if x % 7 == 0 or x % 7 == 6:
            continue
        days.add(x)
    return days
        

n, part = [int(i) for i in input().split()]
days = set()
for x in range(part):
    start, sep = [int(i) for i in input().split()]
    days.update(count_days(n, start, sep))
print(len(days))