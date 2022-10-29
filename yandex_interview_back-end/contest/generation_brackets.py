def combinations(list=[], count=0, len_str=0):
    if len_str == len(list):
        final.append("".join(list))
        return
    if len(list) == 0:
        new_list = list.copy()
        new_list.append("(")
        combinations(new_list, count + 1, len_str)
    if count < len_str - len(list):
        new_list = list.copy()
        new_list.append("(")
        combinations(new_list, count + 1, len_str)
    if count != 0:
        new_list = list.copy()
        new_list.append(")")
        combinations(new_list, count - 1, len_str)


n = int(input())
final = []
combinations(len_str=n * 2)
final = set(final)
for elem in sorted(final):
    print(elem)
