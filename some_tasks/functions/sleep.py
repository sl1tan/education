from time import sleep


def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)


print(delay(lambda x: x / 2, 100, 13))
print(delay(lambda x: x / 2, 1000, 124))
print(delay(lambda x: x / 2, 2000, 12314))
