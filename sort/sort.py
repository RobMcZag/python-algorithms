import random


def swap(lst, i, j):
    """
    swaps the element at position i and j of the given list

    :type lst: list
    :type i: int
    :type j: int
    """
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def insertion(lst):
    """
    sorts a list using the Insertion sort algorithm

    :param lst: the list to be sorted
    :type lst: list
    :return: void
    """
    for idx, val in enumerate(lst):
        for j in range(idx, 0, -1):
            if lst[j-1] <= lst[j]: break
            swap(lst, j, j - 1)


def mergesort(lst):
    """
    sorts a list using the Merge sort algorithm

    :param lst: the list to be sorted
    :type lst: list
    :return: void
    """
    aux = lst[:]
    _mergesort(lst, aux, 0, len(lst))


def _mergesort(lst, aux, st, end):
    if st == end - 1: return    # len 1 is sorted

    m = st + (end-st) / 2
    _mergesort(lst, aux, st, m)
    _mergesort(lst, aux, m, end)
    _merge(lst, aux, st, m, end)


def _merge(lst, aux, st, m, end):
    l = st
    r = m
    aux[st:end] = lst[st:end]
    for idx in range(st, end):
        if l >= m:
            lst[idx] = aux[r]
            r += 1
        elif r >= end:
            lst[idx] = aux[l]
            l += 1
        elif aux[l] <= aux[r]:
            lst[idx] = aux[l]
            l += 1
        else:
            lst[idx] = aux[r]
            r += 1


def quicksort(lst):
    # randomize the list
    random.shuffle(lst)

    # call recursive sort funtion
    _quicksort(lst, 0, len(lst))


def _quicksort(lst, start, end):
    if end - start <= 1:
        return
    # partition the current block
    pos = _partition(lst, start, end)

    # sort block left of partiotining position
    _quicksort(lst, start, pos)
    # sort block right of partiotining position
    _quicksort(lst, pos+1, end)


def _partition(lst, start, end):
    pos = start + 1
    hi = end - 1     # End is NOT included in the array to be partitioned
    while pos <= hi:
        if lst[pos] <= lst[start]:
            pos += 1
        else:
            swap(lst, pos, hi)
            hi += -1
    swap(lst, start, hi)
    return hi
