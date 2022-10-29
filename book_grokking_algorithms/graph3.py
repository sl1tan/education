def find_lowest_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {}
graph["book"] = {"record": 5, "poster": 0}
graph["record"] = {"guitar": 15, "drum": 20}
graph["poster"] = {"guitar": 30, "drum": 35}
graph["guitar"] = {"piano": 20}
graph["drum"] = {"piano": 10}
graph["piano"] = {}

costs = {}
infinity = float("inf")
costs["record"] = 5
costs["poster"] = 0
costs["piano"] = infinity
costs["guitar"] = infinity
costs["drum"] = infinity

parents = {}
parents["record"] = "book"
parents["poster"] = "book"
parents["piano"] = None

processed = []

node = find_lowest_node(costs)
while node != None:
    cost = costs[node]
    neighbors = graph[node]
    for key in neighbors.keys():
        new_cost = cost + neighbors[key]
        if new_cost < costs[key]:
            costs[key] = new_cost
            parents[key] = node
    processed.append(node)
    node = find_lowest_node(costs)

print(costs["piano"])
