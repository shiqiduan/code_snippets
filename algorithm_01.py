#!/usr/local/bin/python
# -*-coding:utf-8-*-
'''
问题描述:
Given a list of people with their birth and end years (all between 1900 and 2000), 
find the year with the most number of people alive.

陷阱1、 a list of people， 数量可能比较大,
陷阱2、累加求最大值

'''

import pprint

pp = pprint.PrettyPrinter()

def main():
    pass


def solution_2(source_data):
    '''
        遍历数据，只处理birth和end两个数据
        输入： [(birth, end), ...]
    '''
    if not source_data:
        return
    aggregate = {}
    for person in source_data:
        birth, end = person
        print birth, end
        if birth >= end:
            continue
        aggregate[birth] = aggregate.get(birth, 0) + 1
        aggregate[end] = aggregate.get(end, 0) - 1
    pp.pprint(aggregate)

    alive_people = 0
    max_alive_people = 0
    max_alive_year = 0
    for year in sorted(aggregate.keys()):
        alive_people = aggregate[year] + alive_people
        if alive_people >= max_alive_people:
            max_alive_people = alive_people
            max_alive_year = year
    print alive_people
    print max_alive_people
    print max_alive_year



if __name__ == '__main__':
    solution_2([(1,5), (1,4), (1,7), (2,6), (2,8)])
