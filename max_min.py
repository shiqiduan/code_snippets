# coding=utf-8
"""
问题:
    在一个具有n的元素的集合中,需要多少次比较才能找到最大值or最小值呢？
    如果同时需要找到最大值和最小值需要执行几次比较？
    有没有改良方法？
"""


def max_value(c=None):
    """
    至少需要比较n-1次
    :param c:
    :return:
    >>> max_value()
    >>> max_value([1,2,3,5])
    5
    >>> max_value([3,4,1,5,7,1,2,3])
    7
    """
    if not c:
        return None
    _max = c[0]
    for i in range(1, len(c)):
        if c[i] > _max:
            _max = c[i]
    return _max


def min_value(c=None):
    """
    至少n-1次
    :return:
    >>> min_value([1,2,3,5])
    1
    >>> min_value([3,4,1,5,7,1,2,3])
    1
    """
    if not c:
        return None
    _min = c[0]
    for i in range(1, len(c)):
        if c[i] < _min:
            _min = c[i]
    return _min


def max_min(c=None):
    """
    同时计算则需要2 * (n - 1).
    但是通过简单的处理， 可以减少到 (n - 1) * 3 / 2
    :param c:
    :return:
    >>> max_min([1,2,3,4,5])
    (5, 1)
    """
    if not c:
        return None, None
    if len(c) == 1:
        return c[0], c[0]
    start = 1 if len(c) % 2 else 0
    _max, _min = c[0], c[0]
    for i in range(start, len(c), 2):
        # 每次至进行三次比较
        temp_max, temp_min = (c[i], c[i+1]) if (c[i] > c[i + 1]) else (c[i+1], c[i])
        if temp_max > _max:
            _max = temp_max
        if temp_min < _min:
            _min = temp_min
    return _max, _min


if __name__ == '__main__':
    import doctest
    doctest.testmod()