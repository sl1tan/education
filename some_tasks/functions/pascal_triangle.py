from turtle import width


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def binominal(n, i):
    return (factorial(n) // (factorial(i) * factorial(n - i)))


def str_pascal(n):
    str = []
    for i in range(0, n + 1):
        str.append(binominal(n, i))
    return str


def triangle(n):
    for i in range(n):
        n_str = str_pascal(i)
        print(" ".join(str(i) for i in n_str))


def nice_str(n):
    last = str_pascal(n)
    last_list = [str(i) for i in last]
    last_str = " ".join(last_list)
    return last_str


def nice_triangle(n):
    last = str_pascal(n)
    last_list = [str(i) for i in last]
    last_str = " ".join(last_list)
    width = len(last_str)

    for i in range(n):
        print(nice_str(i).center(width))


n = int(input())

nice_triangle(n)
