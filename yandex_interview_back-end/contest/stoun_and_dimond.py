decor = input()
stones = input()
count = 0

for stone in stones:
    if stone in decor:
        count += 1

print(count)
