'''
adv
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
L = list(range(100))
print(L[:])
print(L[-10:-1])
# 每5个取一个
print(L[::5])

print('ABCKAJDKF'[:4])

print()

# 迭代
d = {'A':1, 'B':2, 'C':3}
for n in d:
    print(n)

for value in d.values():
    print(value)

for a, b in d.items():
    print(a, b)

print()

for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)

# 列表生成式
print([x * x for x in range(1, 10)])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s for s in L1 if isinstance(s, str)]
print(L2)

print()
# 生成器
g = (x * x for x in range(1, 10))
print(g)
for n in g:
    print(n)

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

n = 1
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# 迭代器
