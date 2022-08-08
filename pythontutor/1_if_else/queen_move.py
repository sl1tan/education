# Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
# Даны две различные клетки шахматной доски, определите,
# может ли ферзь попасть с первой клетки на вторую одним ходом.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

horizontal = y1 == y2
vertical = x1 == x2
diagonal = abs(x1 - x2) == abs(y1 - y2)

if (horizontal or vertical or diagonal):
    print("Yes")
else:
    print("No")
