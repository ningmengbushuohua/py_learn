#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1. 定义
list1 = [34,6,7,'89i',True,[34,89]]
print(list1, type(list1))
tuple1 = (34,6,7,'89i',True,[34,89])
print(tuple1, type(tuple1))

# 注意： 如果元组中只有一个元素，则一定要在元素后面添加逗号，消除歧义，使其表示一个元祖
list2 = [10]
print(list2, type(list2))
tuple2 = ('abc')        # <class 'str'>
print(tuple2, type(tuple2))
tuple2 = ('abc',)       # <class 'tuple'>
print(tuple2, type(tuple2))

# 2. 列表是可变的，元组是不可变的
tuple1 = (34,6,7,'89i',True,[34,89])
# 注意1： 元组一旦定义之后，其中的元素只能访问，无法修改
print(tuple1[0])
print(tuple1[-1])
# tuple1[0] = 88      # 'tuple' object does not support item assignment


# 【面试题】注意2：如果元组中的元素是列表，其中的列表仍然可以修改
print(type(tuple1[-1][0]))
tuple1[-1][0] = 88
print(tuple1)


# 3. 元组中的元素的访问，遍历、切片都和列表相同
t1 = (4,5,6,7,8,9)
print(len(t1))
print(t1[2])

for num in t1:
    print(num)

for i in range(len(t1)):
    print(i, t1[i])

print(t1[::-1])     # (9, 8, 7, 6, 5, 4)
print(t1[88:])      # ()

# 4. 元组 没有增删改，但是有查询功能
print(len(t1))
print(max(t1))
print(min(t1))

print(t1.index(9))
print(t1.count(9))

# 5.列表和 元组可以相互转换
li = [3,5,6]
print(type(li))

ti = tuple(li)
print(type(ti))

l2 = list(ti)
print(type(l2))


# 在实际使用中，常用列表
