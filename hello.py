'''
hello world
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello, world')

#，会输出空格
print('hello', 'world')

#输入
#name = input('input name:')
#print(name)

#use tab ,:后，下一行缩进为代码块
a = 100
if a > 0:
    print(a)
else:
    print(-a)

# r'' 引号内表示不转义
print('\\\t\\')
print(r'\\\t\\')

# '''...''' 交互式命令换行
print('''line1
line2
line3''')
print('\n')
print('''line1
... line2
... line3''')

#test
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#除法
print(9 / 3)
print(9 // 3)   #地板除，只保留整数部分
print(9 % 3)

#输出，和C语言相同
print('%d,%s' % (1,'aa'))
