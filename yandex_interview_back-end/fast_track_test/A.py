def find_min():
    global data
    min_id = min(data, key=data.get)
    print(data[min_id][0])
    data[min_id][0] += data[min_id][1]


def fulfill(string: str):
    global data
    if string == "3":
        find_min()
    else:
        command, row = string.split(maxsplit=1)
        if command == "2":
            data.pop(int(row))
        else:
            a, d, id = [int(i) for i in row.split()]
            data[id] = [a, d]


data = dict()
for x in range(int(input())):
    string = input()
    fulfill(string)
