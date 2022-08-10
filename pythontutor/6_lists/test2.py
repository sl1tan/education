a = list()
print(a)
str = "aboba"
str_list = list(str)
print(str, str_list)
print(str[2], str_list[2])
b = [1] * 5
print(b)
for i in range(len(b)):
    b[i] += 1
print(b)
names = ["Mark", "Bob", "Steve"]
n1, n2, n3 = names
print(n1, n2, n3)
############################
for i in range(len(names)):
    print(names[i])
############################
print()
for name in names:
    print(name)

copy = list(names)
copy.append("2")
print(copy, names)
if copy == names:
    print("COPY = NAMES")
else:
    print("COPY != NAMES")
###########################
d = []
for i in range(4):
    d.append(int(input()))
for elem in d:
    print(elem, end=" ")
