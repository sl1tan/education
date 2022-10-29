words = set()
for x in range(int(input())):
    words = words.union(set(input().split()))
print(len(words))
