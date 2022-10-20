file = open("input.txt")
s = file.readline()
file.close()
a, b = [int(i) for i in s.split()]
file = open("output.txt", mode="w")
print(str(a + b), file=file)