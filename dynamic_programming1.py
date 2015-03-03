#!/usr/local/bin/python
# -*-coding:utf-8-*-
'''
Dynamic Programming
'''
import timeit
import sys
# 修改递归深度的限制
sys.setrecursionlimit(10000)


def fabonacci1(n):
    if n < 3:
        return 1
    return fabonacci1(n - 2) + fabonacci1(n - 1)


def fabonacci2(n):
    if n < 3:
        return 1

    temp_result = {1:1, 2:1}
    value = fabonacci2_dict(n, temp_result)
    return value

def fabonacci2_dict(n, temp_result):
    value = temp_result.get(n)
    if not value:
        value = fabonacci2_dict(n - 2, temp_result) + fabonacci2_dict(n - 1, temp_result)
        temp_result[n] = value
    return value


def fab3(n):
    """
        down to top. 
        时间复杂度和上面的类似，同时也不占用栈空间
    """
    if n < 3:
        return 1
    temp_array = [1] * (n + 1)
    for i in range(3, n+1):
        temp_array[i] = temp_array[i - 2] + temp_array[i - 1]
    return temp_array[n]


def fab4(n):
    """
        线性时间复杂度。 空间复杂度2
    """
    if n < 3:
        return 1
    n1, n2 = 1,1
    for i in range(3, n+1):
        value = n1 + n2
        n1, n2 = n2, value
    return n2


if __name__ == '__main__':
    print timeit.timeit("fabonacci1(30)", setup="from __main__ import fabonacci1", number=1)
    # print timeit.timeit("fabonacci1(40)", setup="from __main__ import fabonacci1", number=1)
    
    print timeit.timeit("fabonacci2(30)", setup="from __main__ import fabonacci2, fabonacci2_dict", number=1)
    print timeit.timeit("fabonacci2(40)", setup="from __main__ import fabonacci2, fabonacci2_dict", number=1)
    print timeit.timeit("fabonacci2(19900)", setup="from __main__ import fabonacci2, fabonacci2_dict", number=1)
    
    print timeit.timeit("fab3(30)", setup="from __main__ import fab3", number=1)
    print timeit.timeit("fab3(19900)", setup="from __main__ import fab3", number=1)
    print timeit.timeit("fab3(100000)", setup="from __main__ import fab3", number=1)

    print timeit.timeit("fab4(30)", setup="from __main__ import fab4", number=1)
    print timeit.timeit("fab4(19900)", setup="from __main__ import fab4", number=1)
    print timeit.timeit("fab4(100000)", setup="from __main__ import fab4", number=1)


