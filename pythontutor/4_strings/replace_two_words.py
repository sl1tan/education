str = input()
space = str.find(" ")
print(str[space + 1:] + " " + str[:space])
