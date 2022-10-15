count = int(input())
dictionary = {}
for x in range(count):
    key, value = input().split()
    dictionary[key] = value
synonym = input()
for key, value in dictionary.items():
    if key == synonym:
        print(dictionary[key])
    if value == synonym:
        print(key)
