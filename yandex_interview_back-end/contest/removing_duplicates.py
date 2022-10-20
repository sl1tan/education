n = int(input())
prev = None
for x in range(n):
    num = int(input())
    if num != prev:
        print(num)
        prev = num
