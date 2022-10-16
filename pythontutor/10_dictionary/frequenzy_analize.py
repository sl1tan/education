words = {}
for x in range(int(input())):
    for word in input().split():
        words[word] = words.get(word, 0) + 1

for_sort = list(words.items())

for_sort.sort(key=lambda x: (x[1] * - 1, x[0]))
for x in for_sort:
    print(x[0])