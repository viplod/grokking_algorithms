def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


def find():
	node = find_lowest_cost_node(costs)
	while node is not None:
		cost = costs[node]
		neighbors = graph[node]
		for n in neighbors.keys():
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost:
				costs[n] = new_cost
				parents[n] = node
		processed.append(node)
		node = find_lowest_cost_node(costs)	

processed = []
graph = {}
graph["start"] =  {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 2
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["c"] = 1
graph["b"]["d"] = 5
graph["c"] = {}
graph["c"]["d"] = 1
graph["c"]["fin"] = 7
graph["d"] = {}
graph["d"]["fin"] = 0
graph["fin"] = {}

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

print(graph)
print(costs)
print(parents)

find()

print('-------')
print(costs)
print(parents)
