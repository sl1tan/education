from math import sqrt

sum = 0
sum_squares = 0
x = int(input())
n = 0
while x != 0:
    n += 1
    sum += x
    sum_squares += x ** 2
    x = int(input())
print(sqrt((sum_squares - sum ** 2 / n) / (n - 1)))
