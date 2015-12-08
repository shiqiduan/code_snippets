# coding=utf-8
"""
  »ùÊýÅÅÐò
"""


def radix_sort(array, radix):
    k = get_number_len(max(array), radix)
    print k
    for i in range(k):
        temp = {x: [] for x in range(radix)}
        for n in array:
            s_n = str(n)
            if i >= len(s_n):
                temp[0].append(n)
            else:
                curr = s_n[-(i + 1)]
                temp[int(curr)].append(n)
        ret = []
        print temp
        for j in range(radix):
            if temp[j]:
                ret.extend(temp[j])
        array = ret
    return array


def get_number_len(num, base):
    assert base > 0
    end = 0 if num >= 0 else -1
    time = 1
    while True:
        ret = num / base
        if ret == end:
            break
        num = ret
        time += 1
    return time


if __name__ == '__main__':
    a = [2, 3, 10, 1, 9, 13, 100, 8, 7]
    print radix_sort(a, 10)
