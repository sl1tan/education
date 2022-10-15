string = input()
words = {}
for word in string.split():
    if word not in words:
        words[word] = 1
        print(0, end=" ")
    else:
        print(words[word], end=" ")
        words[word] += 1
