words = {}
for x in range(int(input())):
    for word in input().split():
        words[word] = words.get(word, 0) + 1

max = max(words.values())
for key in sorted(words.keys()):
    if words[key] == max:
        print(key)
        break
