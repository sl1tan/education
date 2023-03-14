def degree_of_two(count):
    for x in range(count):
        yield 2 ** x


if __name__ == '__main__':
    a = degree_of_two(10)
    for x in a:
        print(x)
