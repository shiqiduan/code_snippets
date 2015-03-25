# coding=utf-8
"""
递归解八皇后问题
"""


def conflict(state, x):
    y = len(state)
    for i in range(y):
        # 处于同一个轴或者对角线上面
        # if state[i] - x == 0 or abs(state[i] - x) == y - i:
        if abs(state[i] - x) in (0, y - i):
            return True
    return False


def queen(num=8, state=()):
    # 最后需要返回的情况
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield (pos,)
    else:
        # 递归
        for pos in range(num):
            if not conflict(state, pos):
                for result in queen(num, state + (pos,)):
                    yield (pos,) + result


def queen1(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queen1(num, state + (pos,)):
                    yield (pos,) + result


def queen2(num=8):
    state = [(x,) for x in range(num)]
    while True:
        if not state:
            return []
        finished = True
        for i in state:
            if len(i) != num:
                finished = False
        if finished:
            return state

        new_state = []
        for i in state:
            for pos in range(num):
                if not conflict(i, pos):
                    new_state.append(i + (pos,))
        state = new_state


if __name__ == '__main__':
    for i in queen2(5):
        print i
