count, balls = [int(i) for i in input().split()]
bowling_field = ["I"] * count
for i in range(balls):
    left, right = [int(i) for i in input().split()]
    bowling_field[left - 1:right] = ["."] * (right - left + 1)
print("".join(bowling_field))
