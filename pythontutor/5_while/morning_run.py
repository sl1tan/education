km = float(input())
max = float(input())
days = 1
while km < max:
    km += km * 0.1
    days += 1
print(days)
