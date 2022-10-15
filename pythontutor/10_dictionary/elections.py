count = int(input())
candidates = {}
for x in range(count):
    surname, voices = input().split()
    voices = int(voices)
    if surname not in candidates:
        candidates[surname] = voices
    else:
        candidates[surname] += voices

surnames = sorted(list(candidates.keys()))
for key in surnames:
    print(key, candidates[key])