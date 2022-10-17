import re

english = {}
for x in range(int(input())):
    string = input()
    word, *synonyms = re.findall(r"\w+", string)
    english[word] = set(synonyms)

latin = {}

for key in english:
    for word in english[key]:
        if word not in latin:
            latin[word] = set([key])
        else:
            latin[word].add(key)

print(len(latin))
for key in sorted(latin):
    print(key, end=" - ")
    print(*latin[key], sep = ", ")

