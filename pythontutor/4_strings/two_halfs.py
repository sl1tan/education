str = input()
len = len(str)
len_2 = len // 2
len_1 = len - len_2
out = str[-len_2:] + str[:len_1] * (len_2 != 0)
print(out)
