a = [int(i) for i in input().split()]
was = set()
for elem in a:
    if elem not in was:
        was.add(elem)
        print("NO")
    else:
        print("YES")