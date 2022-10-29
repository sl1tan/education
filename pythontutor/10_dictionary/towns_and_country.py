towns = {}
for x in range(int(input())):
    country, *town = input().split()
    for city in town:
        towns[city] = country

for x in range(int(input())):
    str = input()
    print(towns[str])
