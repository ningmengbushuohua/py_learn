#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# number = int(input("请输入三位数"))
# num_hundred = number //  100
# num_ten = number - num_hundred * 100 //  10
# num_single = number - num_hundred * 100 - num_ten * 10
# print(f"百位是：{num_hundred}，十位是：{num_ten}，,个位是：{num_single}")
n = 6789
print(n / 1000 % 100)
print(n // 10  % 100 // 10)

x = y = z = 1
print(x)
x = (y == z + 1)
print(x)

# x = (y = z + 1)  等号右边是一个可以计算的 表达式