def question(all):
    good = set()
    while(1):
        inp2 = input()
        if inp2 == "HELP":
            print(*all)
            break
        else:
            inp = set([int(i) for i in inp2.split()])
        answer = input()
        if answer == "YES":
            all.intersection_update(inp)
        elif answer == "NO":
            all.difference_update(inp)

n_max = int(input())
nums = set()
for x in range(1, n_max + 1):
    nums.add(x)

question(nums)