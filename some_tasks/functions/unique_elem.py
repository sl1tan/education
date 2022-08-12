def unique(a):
    res = []
    for elem in a:
        if elem not in res:
            res.append(elem)
    return res


a = [1, 2, 3, 3, 2, 4, 5]
print(unique(a))
