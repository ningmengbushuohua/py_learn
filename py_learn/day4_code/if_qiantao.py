#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.基本使用
# n1 = 34
# n2 = 23
# if n1 != n2:
#     print('yes----ssss')
#     if n1 == 34:
#         print('ssssaaaaaaaaa')
#     else:
#         print('xxxxxx')
# else:
#     print("no---1")

# 2. 应用
'''
x.isdigit():判断x 字符串 是否非空，且全部由数字组成，如果是，则结果为True,反之为Fals
len(x)：字符串的长度
'''
number = input("请输入三位数")
if number.isdigit() and len(number) == 3:
    number = int(number)
    num_hundred = number // 100
    num_ten = (number - num_hundred * 100) // 10
    num_single = number - num_hundred * 100 - num_ten * 10
    print(f"百位是：{num_hundred},十位是：{num_ten},个位是：{num_single}")
else:
    print('输入有误')