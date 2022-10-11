def countdown(i):
    print(i)
    if i > 1:
        countdown(i - 1)

def countdown2(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown2(i - 1)


countdown(3)
countdown2(3)