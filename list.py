'''
list
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list
classmates = ['Micheal', 'Bob']
print(classmates)
print(len(classmates))
print(classmates[-1])

classmates.append("Lima")
print(classmates)

classmates.insert(1, "Jack")
print(classmates)

print('弹出指定元素，无参弹出最后一个')
print(classmates.pop(1))
print(classmates)

# tuple 不可变数组，初始化后不能修改
L = ('A', True, 1)
print(L)

# 一个元素需用 (1,) 定义，因为()有歧义，可以表示小括号
T = (1,)
print(T)
U = (1, 2, [3, 4])
U[2][1] = 5
print(U)

# dict 相对于 map
di = {'Micheal': 20, 'Lily': 30}
di['Jack'] = 40
print(di)
print(di['Micheal'])

# set
sl = [1, 2]
s = set(sl)
print(s)
