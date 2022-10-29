def A(x):
    if x == 1:
        print(x, end=" ")
    else:
        A(x - 1)
        print(x, end=" ")


def B(x, y):
    if x == y:
        print(x, end=" ")
    elif x < y:
        print(x, end=" ")
        B(x + 1, y)
    elif x > y:
        print(x, end=" ")
        B(x - 1, y)


def C(x, y):
    if x == 0:
        return y + 1
    elif x > 0 and y == 0:
        return (C(x - 1, 1))
    elif x > 0 and y > 0:
        return C(x - 1, C(x, y - 1))


def d(x):
    if x == 1:
        return "YES"
    elif x % 2 == 0:
        return d(x / 2)
    else:
        return "NO"


def e(x):
    if x // 10 == 0:
        return x
    else:
        return x % 10 + e(x // 10)


def f(x):
    if x // 10 == 0:
        print(x % 10, end=" ")
    else:
        print(x % 10, end=" ")
        f(x // 10)


def g(x):
    if x // 10 == 0:
        print(x, end=" ")
    else:
        g(x // 10)
        print(x % 10, end=" ")


def h(x, div=2):
    if x == div or div * div > x:
        return "YES"
    elif x % div == 0:
        return "NO"
    else:
        return h(x, div + 1)


def i(x, div=2):
    if x == div:
        print(div, end=" ")
    elif x % div == 0 and h(div) == "YES":
        print(div, end=" ")
        i(x // div)
    else:
        i(x, div + 1)


def j(str):
    if str[0] == str[-1] and len(str) > 1:
        j(str[1:-1])
    else:
        return "NO"
    return "YES"


def k():
    inp = int(input())
    if inp == 0:
        return
    elif inp % 2 == 1:
        print(inp)
    k()


def l():
    inp = int(input())
    if inp == 0:
        return
    inp2 = int(input())
    print(inp)
    if inp2 > 0:
        l()
    else:
        return


def m():
    inp = int(input())
    if inp == 0:
        return 0
    else:
        return max(inp, m())


def n(sum=0, count=0):
    inp = int(input())
    sum += inp
    if inp == 0:
        return sum / count
    else:
        return n(sum, count + 1)


def o(max1=0, max2=0):
    inp = int(input())
    if inp == 0:
        print(max2)
    elif max1 < inp:
        o(inp, max1)
    elif max2 < inp:
        o(max1, inp)
    else:
        o(max1, max2)


def p(max=0, count=1):
    inp = int(input())
    if inp == 0:
        print(count)
    elif inp > max:
        p(inp, 1)
    elif inp == max:
        p(max, count + 1)
    else:
        p(max, count)


def q():
    inp = int(input())
    if inp == 1:
        inp3 = int(input())
        if inp3 == 1:
            return q() + inp + inp3
        else:
            inp4 = int(input())
            if inp4 == 1:
                return q() + inp4 + inp + inp3
            else:
                return inp4 + inp + inp3
    else:
        inp2 = int(input())
        if inp2 == 1:
            return q() + inp + inp2
        else:
            return inp + inp2


def r(n):
    if n == 1:
        return "1"
    else:
        sum = 0
        for x in range(1, n + 1):
            sum += x
            j = str(x)
            if sum > n:
                break
        print(r(n - 1) + j, end=" ")
