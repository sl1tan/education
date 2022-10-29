dict = {}
for x in range(int(input())):
    string = input()
    low = string.lower()
    if low not in dict:
        dict[low] = set()
    dict[low].add(string)

errors = 0
for word in input().split():
    word_low = word.lower()
    if word_low in dict:
        if word not in dict[word_low]:
            errors += 1
    else:
        if len([l for l in word if l.isupper()]) != 1:
            errors += 1

print(errors)
