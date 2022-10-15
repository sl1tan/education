candidates = {}
for _ in range(int(input())):
    surname, voices = input().split()
    candidates[surname] = candidates.get(surname, 0) + int(voices)
for key, value in sorted(candidates.items()):
    print(key, value)
