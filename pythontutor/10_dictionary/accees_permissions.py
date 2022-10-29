ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

files = {}
for x in range(int(input())):
    string = input().split()
    name = string.pop(0)
    files[name] = string

for x in range(int(input())):
    command, name = input().split()
    if ACTION_PERMISSION[command] in files[name]:
        print("OK")
    else:
        print("Access denied")
