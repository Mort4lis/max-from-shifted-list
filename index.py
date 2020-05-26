from typing import List


def max_from_shifted_list(arr: List[int]) -> int:
    """
    Поиск максимального элемента в отсортированном, циклически сдвинутым массивом.

    :param arr: массив целых чисел
    :return: максимальный элемент

    :raise ValueError: если передан пустой список
    """
    if len(arr) == 0:
        raise ValueError('max_from_shifted_list() arg is an empty sequence')

    mid = 0
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (begin + end) // 2

        if arr[mid] < arr[begin]:
            end = mid - 1
        elif arr[mid] < arr[end]:
            begin = mid + 1
        else:
            begin += 1
            end -= 1

    return arr[mid]
