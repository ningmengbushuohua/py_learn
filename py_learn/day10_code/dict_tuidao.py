#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.[面试题]：已知一个字典，dict1 = {'a':10, 'b':20}
# 书写一个程序，实现可以和value 的交换，生成一个新的字典
dict1 = {'a':10, 'b':20}
# 方式一：
dict11 = {}
for key,value in dict1.items():
    dict11[value] = key
print(dict11)

# 方式二       **************
dict12 = dict(zip(dict1.values(),dict1.keys()))
print(dict12)

# 方式三       ****************
dict13 = {value:key for key,value in dict1.items()}
print(dict13)

# 2. 使用字典推导式生成一个字典，{0:0,2:4,6:8,8:64}
# 方式一
dict2 = {num: num ** 2 for num in range(0,9,2)}
print(dict2)

# 方式二
dict21 = {num: num ** 2 for num in range(10) if num % 2 == 0}
print(dict21)

# 3.和列表推导式相同，都可以使用多个for或者 多个if， 执行仍然是 从左往右嵌套的关系
list31 = [m + n for m in 'xyz' for n in '123']
print(list31)       # 9     ['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3']

dict31 = {m : n for m in 'xyz' for n in '123'}
print(dict31)       # 3     {'x': '3', 'y': '3', 'z': '3'}
# 字典的键是唯一的


# 注意：[xx for if] 列表推导式，但是(xx for if) 并不是元组推导式 ，是生成器
list31 = [m + n for m in 'xyz' for n in '123']
print(type(list31))     # <class 'list'>
tuple31 = (m + n for m in 'xyz' for n in '123')
print(type(tuple31))    # <class 'generator'> 生成器：函数中讲解
