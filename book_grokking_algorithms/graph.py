from collections import deque


graph = {}
graph["I"] = ["BOB", "CLAIRE", "ALICE"]
graph["CLAIRE"] = ["TOM", "JOHNY"]
graph["ALICE"] = ["PAGGY"]
graph["BOB"] = ["ANUDJ", "PAGGY"]
graph["PAGGY"] = []
graph["ANUDJ"] = []
graph["TOM"] = []
graph["JOHNY"] = []

search = deque()
search += graph["I"]
searched = []
def person_is_seller(person):
    return person[-1] == "M"

while(search):
    person = search.popleft()
    if person_is_seller(person):
        print("{} is seller!".format(person))
    else:
        searched.append(person)
        search += graph[person]
