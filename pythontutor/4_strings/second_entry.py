str = input()
count = str.count("f")
if count == 1:
    print(-1)
elif count == 0:
    print(-2)
else:
    print(str.find("f", str.find("f") + 1, len(str)))
