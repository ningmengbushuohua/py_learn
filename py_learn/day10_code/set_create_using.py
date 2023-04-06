#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.定义空集合
set11 = set()
print(set11)

# 2.定义非空集合
# a.无序的
set2 = {3,6,7,8,9,10}
print(set2)

# b.无重复元素
set3 = {2,6,6,6,}
print(set3)


# 注意：如果要对列表、元组中的元素进行去重，则可以转换为集合实现   **********


# 3.集合间的运算
s1 = {1,2,3}
s2 = {3,4,5}
# a.交集
print(s1 & s2)      # {3}
print(s1.intersection(s2))  # {3}   **************


# b.并集
print(s1 | s2)      # {1, 2, 3, 4, 5}
print(s1.union(s2))     # ********

# c. 差集
print(s1 - s2)      # {1, 2}
print(s1.difference(s2))    # ********