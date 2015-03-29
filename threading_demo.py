# encoding: utf-8
import threading
import time


# 计时器
# def hello():
#     print "Hello world"

# t = threading.Timer(10, hello)
# t.start()

def task(a, b):
    print a
    time.sleep(1)
    print a
    time.sleep(2)
    print a
    time.sleep(3)
    print a

# for i in range(10):
#     t = threading.Thread(None, task, "test %s" % (i), [i, i+1], {})
#     t.start()

class MyThread(threading.Thread):
    def __init__(self, name):
        # threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print self.name

# for i in range(10):
#     mt = MyThread("name %s" % i)
#     mt.start()

class ParentClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print "i am parent"

    def run(self):
        print "parent %s, %s" % (self.a, self.b)

class Son(ParentClass):
    def __init__(self, name):
        # super(Son, self).__init__("a", "b")
        ParentClass.__init__(self, "a", "b")
        print "i am son %s" % name

    def run(self):
        ParentClass.run(self)
        print "son"

Son("Demo").run()

