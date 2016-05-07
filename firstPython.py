#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 最后的周五
Desc :
"""
# print('hello little motherfucker')

def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass
# manual_iter()
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in frange(0,4,0.5):
    print(n)
array=[1,2,3,4]
it=iter(array)   #invokes array.__iter__()
next(it)         # invoke it.__next__()