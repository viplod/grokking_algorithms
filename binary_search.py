def generate_list(count):
	result = []
	for i in range(1, count-1):
		result.append(i)
	return result


def binary_search(search_list, search_item):
	low = 0
	high = len(search_list) - 1
	count_iteration = 0
	while low <= high:
		count_iteration += 1
		middle = (low + high) // 2
		quess = search_list[middle]
		if quess == search_item:
			return quess, count_iteration
		elif quess < middle:
			high = middle - 1
		else:
			low = middle + 1
	return None, count_iteration


print(binary_search(generate_list(20), 10))