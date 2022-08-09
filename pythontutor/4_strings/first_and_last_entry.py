str = input()
left_entry = str.find("f")
right_entry = str.rfind("f")
if left_entry == right_entry and left_entry != -1:
    print(left_entry)
elif left_entry != -1:
    print(left_entry, right_entry, sep=" ")
