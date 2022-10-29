import math

alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
    if i == 122:
        alphabet.append(" ")


count = int(input())

w = [int(i) for i in input().split()]

for i in range(0, count):
    if i == 0:
        diff = w[i]
    else:
        diff = abs(w[i] - w[i-1])
    pow = int(math.log2(diff))
    print(alphabet[pow], end="")
