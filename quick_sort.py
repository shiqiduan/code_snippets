# coding=utf-8
"""
快速排序，最坏情况n*n, 期望nlogn，原址排序
"""
import random


def quick_sort(array, p, r):
    """
    :param array:
    :param p:
    :param r:
    :return:
    >>> quick_sort([1,2,3,4,5], 0, 4)
    [1, 2, 3, 4, 5]
    >>> quick_sort([5,4,3,2,1], 0, 4)
    [1, 2, 3, 4, 5]
    >>> quick_sort([3,2,1, 5,4,6], 0, 5)
    [1, 2, 3, 4, 5, 6]
    """
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)
    return array


def partition(array, p, r):
    """
    :param array:
    :param p:
    :param r:
    :return:
    >>> partition([1,2,3,6,5,4,7,8, 10, 9], 0, 9)
    8
    >>> partition([1,2,3,4,5], 0, 4)
    4
    >>> partition([1], 0, 0)
    0
    """
    # 选择最后一个元素作为主元，很可能遇到特定的输入触发最坏情况的发生
    x = array[r]
    # 用来标示小于等于主元的范围界限
    i = p - 1
    for j in range(p, r):
        # 如果是小于等于主元的，需要扩大界限，同时因为中间有跳过去的大于主元的元素，所以需要交互。
        if array[j] <= x:
            i += 1
            # 这个是关键
            array[i], array[j] = array[j], array[i]
    # 将主元放在自己的位置上面
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1


# ###########################################

def random_quick_sort(array, p, r):
    """
    :param array:
    :param p:
    :param r:
    :return:
    >>> random_quick_sort([1,2,3,4,5], 0, 4)
    [1, 2, 3, 4, 5]
    >>> random_quick_sort([5,4,3,2,1], 0, 4)
    [1, 2, 3, 4, 5]
    >>> random_quick_sort([3,2,1, 5,4,6], 0, 5)
    [1, 2, 3, 4, 5, 6]
    """
    if p < r:
        q = random_partition(array, p, r)
        random_quick_sort(array, p, q - 1)
        random_quick_sort(array, q + 1, r)
    return array


def random_partition(array, p, r):
    # 随机选择主元，避免最坏情况发生
    x = random.randint(p, r)
    array[r], array[x] = array[x], array[r]
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1


if __name__ == "__main__":
    if __name__ == '__main__':
        import doctest
        doctest.testmod()