#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  is
# is not
# 1.int/float/str/bool/tuple 不可变的数据类型
a = 10
b = 10
print(a == b)   # True
print(a is b)   #True
print(id(a), id(b))

c = 20
print(a==c) # False
print(a is c)   # False

# 2. list/dict/ set: 可变的数据类型
list1 = [1, 2 ,3]
list2 = [1, 2 ,3]   # 重新开辟一个地址
print(list1 == list2)   # True
print(list1 is list2)   # False,

list3 = [1, 2 ,4]
print(list1 == list3)   # False
print(list1 is list3)   #False

# 结论：
# 如果两个变量的地址相同， 则这两个变量存储的数据 一定相同
# 如果两个变量的存储的数据相同， 则这两个变量的地址不一定相同