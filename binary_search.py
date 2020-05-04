"""Модуль осуществляет бинарный поиск по генерируемому списку целых чисел."""


def generate_list(count):
    """Функция создает список целых чисел от 1 до входного значения.

    Args:
        count (int): Количество создаваемых эелементов в списке

    Returns:
        new_list(list): Список целых чисел.
    """
    new_list = []
    for elem in range(1, count + 1):
        new_list.append(elem)
    return new_list


def binary_search(search_list, search_item):
    """Функция осуществляет бинарные поиск в списке.

    Args:
        search_list (list): Список целых чисел, в котором осуществляется поиск
        search_item (Int): Элемент, который надо найти в списке

    Returns:
        guess or None (Int): Найденный элемент или None
        count_iteration (Int): Количество итераций цикла поиска
    """
    low = 0
    high = len(search_list) - 1
    count_iteration = 0
    while low <= high:
        count_iteration += 1
        middle = (low + high) // 2
        quess = search_list[middle]
        if quess == search_item:
            return quess, count_iteration
        elif quess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return None, count_iteration


if __name__ == '__main__':
    print(binary_search(generate_list(11200), 1))
