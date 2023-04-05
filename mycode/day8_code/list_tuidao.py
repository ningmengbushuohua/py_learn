#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
语法：[新列表中元素的规律 for循环 if判断]
工作原理：指定for循环，获取已知iterable【容器】中的元素，结合if进行判断，最终得到新的列表中元素的规律
作用：生成列表
'''

# 1. 已知list1 = [2,56,6,65,89,14,93],生成一个新的列表，该列表中的元素 是list1 中的2 倍
list1 = [2,56,6,65,89,14,93]
# 方式一
list11 = []
for num in list1:
    list11.append(num * 2)
print(list11)

# 方式二
list12 = [2 * num for num in list1]     # if可以省略
print(list12)

# 2. 将1-100 之间 的所有的奇数挑出来，生成新的列表
list21 = []
for n in range(1,101,2):
    list21.append(n)
print(list21)

list22 = [n for n in range(1,101,2)]
print(list22)

list21 = []
for n in range(1,101):
    if n % 2 ==1:
        list21.append(n)
print(list21)

list22 = [n for n in range(1,101) if n % 2 == 1]
print(list22)

# 3. 注意： 在列表推导式中 ，for循环和 if 语句都可以根据需求书写多个, 从左往右是嵌套的关系

# a.
list31 = [m + n for m in '123' for n in 'xyz']
print(list31)
# 工作原理
list31 = []
for m in '123':
    for n in 'xyz':
        list31.append(m + n)
print(list31)

# b.
list32 = [n for n in range(1,100) if n % 3 == 0 if n % 5 == 0]
print(list32)

# 工作原理
list32 = []
for n in range(1,100):
    if n % 3 == 0:
        if n % 5 == 0:
            list32.append(n)
print(list32)

# 练习： 已知 numlist = [34,56,89,94,92,15,36,7,89,20],删除列表中3的倍数
numlist = [34,56,89,94,92,15,36,7,89,20]
# 错误写法
# numlist_new = [numlist.remove(num) for num in numlist if num % 3 == 0]
# print(numlist_new)  # [None]
# numlist.remove(num)   # None

# 正确写法
numlist_new = [num for num in numlist if num % 3 != 0]
print(numlist_new)  #[34, 56, 89, 94, 92, 7, 89, 20]

numlist_new = []
for num in numlist:
    if num % 3 !=0:
        numlist_new.append(num)
print(numlist_new)
