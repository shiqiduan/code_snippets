import quick_sort

def random_select(array, p, r, i):
    """
    :param array:
    :param p:
    :param r:
    :param x:
    :return:
    >>> random_select([1,2,3,4,5], 0, 4, 3)
    3
    >>> random_select([1,2,3,4,5], 0, 4, 1)
    1
    >>> random_select([1,2,3,4,5], 0, 4, 5)
    5
    >>> random_select([5, 4, 3, 1, 2], 0, 4, 2)
    2
    """
    if p == r:
        return array[p]
    q = quick_sort.random_partition(array, p, r)
    k = q - p + 1
    if k == i:
        return array[q]
    elif i < k:
        return random_select(array, p, q - 1, i)
    else:
        return random_select(array, q + 1, r, i - k)


if __name__ == "__main__":
    if __name__ == '__main__':
        import doctest
        doctest.testmod()