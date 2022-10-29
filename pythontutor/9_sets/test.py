a = {1, 2, 2, 3}
b = {1, 3}
d = {4, 5}
c = a.union(b)
c.update(d)
e = a.intersection(b)
print(c, e)
x = {1}
y = {2, 3}
print(x.intersection_update(y))
# print(a.difference(b))
v = {1, 2, 3}
z = {1, 3}
m = v.difference_update(z)
a = {1, 2, 3, 7}
b = {4, 5, 6, 7}
print(a.symmetric_difference(b))
x = {1, 2}
y = {1, 2, 3}
z = {4, 5}
print(y.issubset(x))
a = [2, 10, 4]
print(sorted(a))
a = {"231", "abobA"}
print(a)
