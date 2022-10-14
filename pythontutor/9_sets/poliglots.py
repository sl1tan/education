all_know = set()
one_know = set()
max = 0
buff = []
for x in range(int(input())):
    for y in range(int(input())):
        lang = input()
        buff.append(lang)
        one_know.update(set(buff))
    if x == 0:
        all_know.update(one_know)
    all_know &= one_know
    if len(one_know) > max:
        max_set = one_know.copy()
        max = len(one_know)
    one_know.clear()
    buff.clear()

print(len(all_know))
print(*sorted(all_know), sep = "\n")
print(len(max_set))
print(*sorted(max_set), sep = "\n")