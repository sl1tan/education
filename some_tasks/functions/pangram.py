from curses.ascii import isalpha


def isPangram(str):
    alph = []
    s = str.lower()
    for i in range(len(s)):
        if isalpha(s[i]) and s[i] not in alph:
            alph.append(s[i])
    return len(alph) == 26


print(isPangram("The quickkkkk brown fox jumps over the lazy dog"))
