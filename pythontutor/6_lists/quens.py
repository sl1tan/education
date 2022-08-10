field = []
flag = 0
for i in range(8):
    x, y = [int(i) for i in input().split()]
    field.append(x)
    field.append(y)
for i in range(0, len(field), 2):
    for j in range(i, len(field), 2):
        diagonal_check = abs(field[i] - field[j]
                             ) == abs(field[i + 1] - field[j + 1])
        x_check = field[i] == field[j]
        y_check = field[i + 1] == field[j + 1]
        is_intersection = diagonal_check or x_check or y_check
        if i != j and is_intersection:
            flag = 1
print("YES" if flag else "NO")
