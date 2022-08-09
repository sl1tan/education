angle = float(input())
hours = angle // 30
minutes = angle % 30 // 0.5
seconds = angle % 30 % 0.5 // 0.008333333
print("%d %d %d" % (hours, minutes, seconds))
