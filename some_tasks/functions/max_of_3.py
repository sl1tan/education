def max3(a, b, c):
    max = b if b > a else a
    max = c if c > max else max
    return max


print(max3(1, 2, 3))
