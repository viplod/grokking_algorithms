def quicksort(array):
	if len(array) < 2:
		return array
	else:
		index = len(array) // 2
		pivot = array[len(array) // 2]
		less = [i for i in array[:index] if i <= pivot] + [i for i in array[index + 1:] if i <= pivot]
		greater = [i for i in array[:index] if i > pivot] + [i for i in array[index + 1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([5, 3, 8, 1, 2, 6, 4, 7]))