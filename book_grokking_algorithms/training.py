def A(x):
    if x == 1:
        print(x, end=" ")
    else:
        A(x - 1)
        print(x, end=" ")

def B(x, y):
    if x == y:
        print(x, end = " ")
    elif x < y:
        print(x, end = " ")
        B(x + 1, y)
    elif x > y:
        print(x, end = " ")
        B(x - 1, y)

def C(x, y):
    if x == 0:
        return y + 1
    elif x > 0 and y == 0:
        return(C(x - 1, 1))
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
        print(x % 10, end = " ")
    else:
        print(x % 10, end = " ")
        f(x // 10)

def g(x):
    if x // 10 == 0:
        print(x, end = " ")
    else:
        g(x // 10)
        print(x % 10, end = " ")
        
def h(x, div = 2):
    if x == div or div * div > x:
        return "YES"
    elif x % div == 0:
        return "NO"
    else:
        return h(x, div + 1) 

def i(x, div = 2):
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
    if  inp == 0:
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
    inp = int(input(0))
    if inp == 0:
        return

m()