from curses.ascii import islower, isupper


def count_lower_letters(a):
    count = 0
    for elem in a:
        if islower(elem):
            count += 1
    return count


def count_upper_letters(a):
    count = 0
    for elem in a:
        if isupper(elem):
            count += 1
    return count


def count_low_and_upper_letters(a):
    low = count_lower_letters(a)
    up = count_upper_letters(a)
    return [low, up]


a = input()
count = count_low_and_upper_letters(a)
print(count)
