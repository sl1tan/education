def evclid(x, y):
    maxi = max(x, y)
    mini = min(x, y)
    if maxi % mini == 0:
        return mini
    else:
        return evclid(maxi - mini * (maxi // mini), mini)


print(evclid(1680, 640))
