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

def merge(lst):
    """
    sorts a list using the Merge sort algorithm

    :param lst: the list to be sorted
    :type lst: list
    :return: void
    """
    aux = lst[:]
    _mergeSort(lst, aux,  0, len(lst))

def _mergeSort(lst, aux, st, end):
    if st == end - 1 : return    # len 1 is sorted

    m = st + (end-st) / 2
    _mergeSort(lst, aux, st, m)
    _mergeSort(lst, aux, m, end)
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
