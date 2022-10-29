n = int(input())
count = 0
max_count = 0
for x in range(n):
    num = int(input())
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)
