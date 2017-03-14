# -*-coding:utf-8-*-

'''
    求最长连续回文串
'''

def solution(array):
    if not array:
        return None
    # 忽略全部一样的情况
    start,end,mid,flag = 0, 0, 0, False
    max_len = 1
    for i in range(len(array)):
        if i == len(array) - 1:
            # 最后一个元素
            continue
        current = array[i]
        next = array[i + 1]

        if next - current == 1: # 向上
            if flag: # 向上中
                end = end + 1
                mid = end
                flag = True
            else: # 向下转向上
                max_len = max(max_len, (end - mid) * 2 + 1)
                flag = True
                print start,end,mid,flag
                start,end,mid = i, i + 1, i + 1
            continue

        if next - current == -1: # 向下
            end = end + 1
            if flag: # 向上转向下
                mid = i
                flag = False
            else: # 连续向下，必要避免超出了start
                flag = False
            continue

        max_len = max(max_len, (end - mid) * 2 + 1)
        print start,end,mid,flag
        start,end,mid = i, i, i
        i = i + 1

    print "end",start,end,mid,flag
    print max_len




if __name__ == "__main__":
    # example = [1,2,1,2,3,2,1,3,1,2,3,4,3,2,1,1]
    # example = [1,2,3,2,1,1,1,1,1,1]
    example = [1,2,1,2,1,2]
    solution(example)
