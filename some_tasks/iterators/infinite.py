def infinite(list, tries):
    iterator = iter(list)
    res = ''
    for x in range(tries + 1):
        try:
            res += str(next(iterator))
            # res.join(str(next(iterator)))
        except StopIteration:
            iterator = iter(list)
    return res


if __name__ == '__main__':

    print(infinite([1, 2], 3))
    print(infinite([], 3))
    print(infinite(['2', '3'], 3))
    print(infinite([1, 2], 0))



