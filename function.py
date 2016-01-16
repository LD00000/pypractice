'''
function
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

print(power(2, 3))


def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n
    return sum

print(calc(1, 2, 3))

def person(name, age, **kw):
    if 'Kate' in kw:
        pass

def person2(name, age, *, job, city='beijing'):
    print(name, age, job, city)
