str = input()
count = 0
for i in range(len(str)):
    if i % 3 == 0:
        str = str.replace(str[i + count], "", 1)
        count -= 1
print(str)
