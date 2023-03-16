def fibonacci(n):
    left, right = 1, 1
    for x in range(n):
        if x == 0:
            yield 1
        elif x == 1:
            yield 1
        else:
            left, right = right, left + right
            yield right


f = fibonacci(30)

for x in f:
    print(x)
