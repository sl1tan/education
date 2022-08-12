def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        cortage = zip(trow+y, y+trow)
      #   print(cortage)
        trow = [l+r for l, r in cortage]
    return n >= 1


pascal_triangle(6)
