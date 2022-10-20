from collections import Counter


first = input()
second = input()

arr = Counter(first)
arr2 = Counter(second)

print(1 *( arr == arr2))

