def is_ancestor(man, older_man):
    if man == older_man:
        return True
    while man in p_tree:
        man = p_tree[man]
        if man == older_man:
            return True
    return False


def lca(member1, member2):
    if member1 == member2:
        return member1
    if is_ancestor(member1, member2):
        return member2
    elif is_ancestor(member2, member1):
        return member1
    else:
        return lca(member1, p_tree[member2])


p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

for i in range(int(input())):
    first, second = input().split()
    LCA = lca(first, second)
    if LCA == None:
        print()
    else:
        print(LCA)