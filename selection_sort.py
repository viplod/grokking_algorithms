"""Модуль осуществляет сортировку выбором массива целых чисел."""


import random


def generate_array(count):
    """Функция создает массив целых чисел от 1 до входного значения.

    Args:
        count (int): Количество создаваемых элементов в списке.

    Returns:
        new_arr(list): Список целых чисел.
    """
    new_arr = random.sample(range(count), count)
    print(new_arr)
    return new_arr


def find_smallest(arr):
    """Функция ищет наименьшее значение в массиве и возвращем ее индекс.

    Args:
        arr (list): Список целых чисел.

    Returns:
        min_index (Int): Индекс минимального числа.
    """
    min_elem = arr[0]
    min_index = 0
    for index in range(0, len(arr)):
        if min_elem > arr[index]:
            min_elem = arr[index]
            min_index = index
    return min_index


def selection_sort(arr):
    """Функция осуществляет сортировку выбором в списке.

    Args:
        arr (list): Список целых чисел, в котором осуществляется сортировка.

    Returns:
        new_arr (list): Отсортированный список.
    """
    new_arr = []
    for index in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    print(selection_sort(generate_array(20)))


