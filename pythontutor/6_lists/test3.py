

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
len = len(a)
# for i in range(0, len, 2):
#     a.insert(i, 0)
a.extend(b)
a.remove(3)
b.clear()
print(b)
print(a)
print(a.index(4, 0, -1))
print(a.pop(2))
print(a)
print(a.count(5))
a.append(0)
a.sort(reverse=True)
print(a)
c = a.copy()
print(c)
print("min = %d, max = %d" % (min(c), max(c)))
stroka = "aASDsd"
stroka.lower()
print(stroka)
print(stroka[1:4])
e = list(stroka)
e.reverse()
print(e)
