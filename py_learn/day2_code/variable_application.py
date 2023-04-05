#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 交换两个变量的值
# A .增加中间变量
num1 = 23
num2 = 88
tmp_num = num1
num1 = num2
num2 = tmp_num
print(num1, num2)

# B,python 特有
num1 = 23
num2 = 88
num1, num2 = num2, num1

print(num1, num2)

# C 方式三：加减法
num1 = 23
num2 = 88
num1 = num1 + num2  # 23+88
num2 = num1 - num2  # 23+88 -88
num1 = num1 - num2  # 23+ 88 -23

# 方式4 ：异或

# 2. 打包 pack和拆包 unpack

# a. 打包
b1, b2, *b3 = 45, 56, 89, 56, 89
print(b1, b2,b3)

b1, *b2, b3 = 45, 56, 89, 56, 89
print(b1, b2,b3)

*b1, b2, b3 = 45, 56, 89, 56, 89
print(b1, b2,b3)

# B.拆包
a,b,c =[56,65,58]
print(a,b, c)

a,b,c =(56,65,58)
print(a,b,c)

a,b,*c =(56,65,58,89,56,45)
print(a,b,c)

