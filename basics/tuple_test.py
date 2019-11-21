# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:51:36 2019

@author: Sekhar
"""

numbers = (2, 4, 5, 3, 2, 5)

print(type(numbers))

li = list(numbers)

print(type(li))

li[0] = 1

for number in li:
    print(number)



x, y, z = [2, 4, 7]

print('x: '+str(x))
print('y: '+str(y))

s = 'abcd'
L = [10, 20, 30, 40]
z = zip(s,L)
print(list(z))

from datetime import datetime
d = datetime(1,1,1).now()
print(d)

am_pm = 'am' if d.hour<12 else 'pm'
print('{}:{}{}'.format(d.hour%12, d.minute, am_pm))