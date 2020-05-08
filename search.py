from collections import deque

def  person_is_seller(name):
	return name[-1] == '1'


def search(name):
	search_queue = deque()
	search_queue += graph[name]
	print(search_queue)
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a mango seller!")
				return True
			else:
				search_queue += graph[person]
				print(search_queue)				
				searched.append(person)
	return False



graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peqqy"]
graph["alice"] = ["peqqy"]
graph["claire"] = ["thom", "jonny1"]
graph["anuj"] = []
graph["peqqy"] = []
graph["thom"] = []
graph["jonny1"] = []



print(search("you"))