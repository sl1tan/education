def sort(a):
    str = a.split("-")
    str_sorted = sorted(str)
    res = "-".join(str_sorted)
    return res


print(sort("green-red-yellow-black-white"))
