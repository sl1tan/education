n = int(input())
lesson = 45
time = 540
time += lesson * n + (n // 2 * 5) + ((n + 1) // 2 - 1) * 15
hours = time // 60
minutes = time % 60
print("{} {}".format(hours, minutes))
