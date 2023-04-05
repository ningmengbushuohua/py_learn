#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 个元素
元素：     11   22  33  44  55  66  77  88  99
正数索引：  0    1   2   3   4   5   6   7   8
负数索引： -9   -8  -7  -6   -5  -4  -3  -2  -1

索引的取值范围：
    正数索引：0~len(x) - 1
    负数索引：-len(x) ~ -1
"""

print([45,5,2,6,56,98]) #有序的，有索引
print({45,5,2,6,56,98}) # 无序的，无索引

list1 = [11,22,33,44,55,66,77,88,99]
print(list1)
print(len(list1))   # 获取列表的长度 或者 获取列表的元素的个数

# 1.获取
# 语法： 列表[索引]， 字符串和元组的访问方式 也是如此
print(list1[0])
print(list1[-9])

print(list1[4])
print(list1[-5])

print(list1[len(list1) - 1])
print(list1[-1])

# 注意： 如果要访问列表中的元素，切记不要索引越界
# print(list1[100])       # IndexError: list index out of range 列表索引越界
#print(list1[-100])         # IndexError: list index out of range

# 2. 修改
# 语法 ：列表[索引] = 值

print(list1)
list1[0] = 'asss'
list1[5] = '595'
print(list1)

