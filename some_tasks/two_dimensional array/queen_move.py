def make_field():
    field = [['.'] * 8 for i in range(8)]
    return field


def out2d(arr):
    for row in arr:
        for i in row:
            print("%2c" % (i), end="")
        print()


def horse(field, x, y):
    if 0 <= x + 1 <= 7 and 0 <= y - 2 <= 7:
        field[x + 1][y - 2] = '*'
    if 0 <= x + 1 <= 7 and 0 <= y + 2 <= 7:
        field[x + 1][y + 2] = '*'
    if 0 <= x + 2 <= 7 and 0 <= y - 1 <= 7:
        field[x + 2][y - 1] = '*'
    if 0 <= x + 2 <= 7 and 0 <= y + 1 <= 7:
        field[x + 2][y + 1] = '*'
    if 0 <= x - 1 <= 7 and 0 <= y - 2 <= 7:
        field[x - 1][y - 2] = '*'
    if 0 <= x - 1 <= 7 and 0 <= y + 2 <= 7:
        field[x - 1][y + 2] = '*'
    if 0 <= x - 2 <= 7 and 0 <= y - 1 <= 7:
        field[x - 2][y - 1] = '*'
    if 0 <= x - 2 <= 7 and 0 <= y + 1 <= 7:
        field[x - 2][y + 1] = '*'

def queen(field, x2, y2):
    for x in range(8):
        for y in range(8):
            horyzontal = y == y2
            vertical = x == x2
            diagonal = abs(x - x2) == abs(y - y2)
            if (horyzontal or vertical or diagonal):
                field[x][y] = "*"


field = make_field()

position = input()

column = position[0]
row = int(position[1])

for i in range(26):
    if column == chr(97 + i):
        column = i + 1


queen(field, abs(row - 8), column - 1)
field[abs(row - 8)][column - 1] = "Q"

out2d(field)