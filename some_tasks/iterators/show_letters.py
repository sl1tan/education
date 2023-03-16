def show_letters(some_str):
    clean_str = ''.join([letter for letter in some_str if letter.isalpha()])
    for symbol in clean_str:
        yield symbol

def my_show_letters(some_str: str):
    for symbol in some_str:
        if symbol.isalpha():
            yield symbol


def t_show_letters(some_str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])


if __name__ == '__main__':
    s = show_letters('13fsa21sda')
    for x in s:
        print(x)
    s2 = my_show_letters('13fsa21sda')
    for x in s2:
        print(x)
    s3 = t_show_letters('13fsa21sda')
    for x in s3:
        print(x)
