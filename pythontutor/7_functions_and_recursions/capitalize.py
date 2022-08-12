def capitalize(a):
    b = a.split()
    for i in range(len(b)):
        elem = b[i]
        up = chr(ord(elem[0]) - 32)
        new = ""
        for j in range(0, len(elem)):
            if j == 0:
                new += up
            else:
                new += elem[j]
        b[i] = new
    return " ".join(b)


a = input()
print(capitalize(a))
