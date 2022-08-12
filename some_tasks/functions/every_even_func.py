def even(a):
    res = []
    for elem in a:
        if elem % 2 == 0:
            res.append(elem)
    return res


a = [int(i) for i in range(0, 10)]
print(even(a))
