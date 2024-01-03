#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一： 引用赋值
# 注意： 引用赋值对于 可变的数据类型(list、dict、set)而言，在使用的过程中意义不大，无法达成备份的目的
# 所以使用=进行赋值，常用于不可变（字符串、数字、元组）的数据类型
list1 = [1,2,3]
list2 = list1
list1[0]= 100

print(list1)
print(list2)
print(list1 is list2) # True
# 二：浅拷贝：列表.copy() / copy.copy()  /切片
# a.
import  copy
list1 = [1,2,3]
list2 = list1.copy()
# list2 = copy.copy(list1)
# list2 = list1[:]
list1[0]= 100

print(list1)    # [100,2,3]
print(list2)    # [1,2,3]
print(list1 is list2)   # False

# is 判断地址 ，等号判断数据  # 身份运算符

print("*" * 50)

# b.
list1 = [1,2,[2,3,6]]
list2 = list1.copy()

list1[-1][0]= 100

print(list1)    # [1, 2, [100, 3, 6]]
print(list2)    # [1, 2, [100, 3, 6]]
print(list1 is list2) # False
print(list1[-1] is list2[-1])   # True

# 三： 深拷贝
# a.
list1 = [1,2,3]
list2 = copy.deepcopy(list1)
list1[0]= 100

print(list1)    # [100,2,3]
print(list2)    # [1,2,3]
print(list1 is list2)   # False

# b.
list1 = [1,2,[2,3,6]]
list2 = copy.deepcopy(list1)

list1[-1][0]= 100

print(list1)    # [1, 2, [100, 3, 6]]
print(list2)    # [1, 2, [2, 3, 6]]
print(list1 is list2) # False
print(list1[-1] is list2[-1])   # False

