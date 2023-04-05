#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.已知一个数字列表，打印列表中的偶数元素
numlist = [1,56,6,6,6,3,3,2,8,826,14,7]
for num_temp in numlist:
    if num_temp % 2 == 0:
        print(num_temp)
# 2.已知任意一个列表，打印列表中索引为偶数的元素
numlist = [1,56,6,6,6,3,3,2,8,826,14,7]
for index in range(len(numlist)):
    if index % 2 == 0:
        print(numlist[index])

for i in range(0, len(numlist), 2):
    print(numlist[i])
# 3.已知一个数字列表,求列表中的元素和
numlist = [1,56,6,6,6,3,3,2,8,826,14,7]
# 方式 一：
total = 0
for num in numlist:
    total += num
print(total)

# 方式二：
total = sum(numlist)
print(total)

