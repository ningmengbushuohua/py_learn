#!/usr/bin/env python3
# -*- coding: utf-8 -*-
dict1 = {"小明":88, 'age':18, '阿哥':18}
print(dict1)
# 方式一：          *********
for r in dict1:     # key
    print(r)

for key in dict1:
    print(key,dict1[key])

print('*' * 20)
# 方式二：
# print(dict1.keys())
for key in dict1.keys():
    print(key,dict1[key])

print('*' * 20)

#  方式三：
print(dict1.values())
for value in dict1.values():
    print(value)

print('*' * 20)

# 方式四：      ******
print(dict1.items())
for r in dict1.items():
    print(r)
# ('小明', 88)
# ('age', 18)
# ('阿哥', 18)

for key,value in dict1.items():     # 拆包
    print(key,value)
