#!/usr/local/bin/python
# -*-coding:utf-8-*-
'''
    Python 多进程的计数器
'''

from time import sleep
from ctypes import c_int
from multiprocessing import Value, Lock, Process

counter = Value(c_int)  # defaults to 0
counter_lock = Lock()
def increment():
    # with counter_lock:
    #     counter.value += 1
    counter.value += 1

def do_something():
    increment()
    print counter.value

for i in range(1000):
    Process(target=do_something).start()

sleep(3)
print counter.value