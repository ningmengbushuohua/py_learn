#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#三目运算符
# 语法 a if 条件 else b
# 原理：条件成立，结果为a, 否则为 b
# 1.exmple
num = 2
num_y = 26 if num == 2 else 26

# 2. 代码块：逻辑复杂
num = int(input("请输入一个数据："))
# 注意： =： 赋值， ==:比较
if num % 2 == 0:
    print("该数是偶数")
else:
    print(f'{num}是奇数')

# 3.三目运算： 逻辑简单
num = int(input("请输入一个数据："))
r1 = '偶数' if num % 2 == 0 else '奇数'
print(r1)
