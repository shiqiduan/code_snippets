# -*-coding:utf-8-*-

'''
    求连续子数组最大和
'''

def solution_n3(array):
    if not array:
        return None
    max_sum = array[0]
    for i in range(len(array)):
        for j in range(i, len(array)):
            local_sum = 0
            for k in range(i, j + 1):
                local_sum += array[k]
            if local_sum >= max_sum:
                max_sum = local_sum
    return max_sum


def solution_n2(array):
    if not array:
        return None
    max_sum = array[0]
    for i in range(len(array)):
        local_sum = 0
        for j in range(i, len(array)):
            local_sum += array[j]
            if local_sum >= max_sum:
                max_sum = local_sum
    return max_sum


def solution_n(array):
    if not array:
        return None
    max_sum = array[0]
    substitute_max_sum = 0
    for i in array:
        substitute_max_sum = substitute_max_sum + i
        if substitute_max_sum > max_sum:
            max_sum = substitute_max_sum
        if substitute_max_sum <= 0:
            substitute_max_sum = 0
    return max_sum


def solution_nlogn(array):
    if not array:
        return None
    return solution_nlogn_recursion(array, 0, len(array) - 1)

def solution_nlogn_recursion(array, start, end):
    if start == end:
        return array[start]
    if start + 1 == end:
        return max(array[start], array[end], array[start] + array[end])
    mid = (start + end) / 2
    max_sum = max(max_sum_with_mid(array, start, end, mid), solution_nlogn_recursion(array, start, mid - 1), 
        solution_nlogn_recursion(array, mid + 1, end))
    return max_sum

def max_sum_with_mid(array, start, end, mid):
    '''
        solution_n 的方法与这里的计算只是多了一个条件来清空substitute_max_sum
    '''
    def max_sum_with_range(array, start, end, mid, range_array):
        max_sum = array[range_array[0]]
        substitute_max_sum = 0
        for i in range_array:
            substitute_max_sum = substitute_max_sum + array[i]
            if substitute_max_sum > max_sum:
                max_sum = substitute_max_sum
        return max_sum

    max_right = max_sum_with_range(array, start, end, mid, range(mid, end + 1))
    max_left = max_sum_with_range(array, start, end, mid, range(mid, start - 1, -1))
    return max_left + max_right - array[mid]


def test_scaffold(solution):
    a = [
        ([1,2,3,4,5,6], 21),
        ([-1,-2,-1,-2,-1], -1),
        ([1,-1,1,-1,1,-1], 1),
        ([-1, 0, -1, 0, -1], 0),
        ([-1,-1,-1,-1, 1], 1),
        ([9, -1,-1,-1], 9),
        ([-1,-1,-1,5,-1,-1,-1], 5),
        ([9, -1,-1,-1, 4], 10),
        ([], None),
        (None, None)
    ]

    for subarray in a:
        result = solution(subarray[0])
        exp1 = result == subarray[1]
        exp2 = "%s, %s, expect : %s,  actual : %s" % (solution.__name__, subarray[0], subarray[1], result)
        assert exp1, exp2

if __name__ == "__main__":
    test_scaffold(solution_n3)
    test_scaffold(solution_n2)
    test_scaffold(solution_n)
    test_scaffold(solution_nlogn)

    # print max_with_limit([1,-1,1,-1,1,-1], 0, 5, 2)

