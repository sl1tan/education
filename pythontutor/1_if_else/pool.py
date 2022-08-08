n = int(input())
m = int(input())
x = int(input())
y = int(input())

ma = max(n, m)
mi = min(n, m)

if x >= ma / 2:
    x = ma - x
if y >= mi / 2:
    y = mi - y


print(min(x, y))