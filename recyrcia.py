def rec(num):
	print(num)
	if num <= 0:
		return
	rec(num - 1)

#rec(50)


def get_sum(num):
	if num // 10 == 0:
		return num
	return num % 10 + get_sum(num // 10 )

#print(get_sum(12345))

def get_len_list(list):
	if list == []:
		return 0
	return 1 + get_len_list(list[1:])

#print(get_len_list([2, 2, 2]))

def get_max(list):
	if len(list) == 1:
		return list[0]
	return max(list[0], get_max(list[1:]))

#print(get_max([1, 5, 3, 25, 7, 150]))

def binary_search(slist, elem):
    middle = len(slist) // 2
    print(slist)
    print(middle)
    quess = slist[middle]
    if quess == elem:
            return quess
    elif quess > elem:
        return binary_search(slist[:middle - 1], elem)
    elif:
        return binary_search(slist[middle + 1:], elem)


print(binary_search([1, 2, 3, 4, 5], 4))

