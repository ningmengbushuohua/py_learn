#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list1 = [11,22,33,44,55,66,77,88,99]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[6])
print(list1[7])
print(list1[8])

print('*' * 52)
# 方式一：只获取 元素
for li in list1:
    print(li, end = ' ')

print('*' * 52)
# 方式二： 获取索引----> 列表[索引]
# n = 0
# while n < len(list1):
#     print(list1[n], end=' ')
#     n += 1

for n in range(len(list1)):
    print(list1[n])

# 方式三：enumerate() ，可以同时获取索引 和元素
# 将 enumerate(x), 将 x 转换为 枚举 ，仍然是一个容器，
# 只不过 该容器存储的是 索引 + 元素
# print(enumerate(list1))
# print(list(enumerate(list1)))
for n, num in enumerate(list1): # 拆包 元组中的数据拆成两个变量
    print(n, num)

