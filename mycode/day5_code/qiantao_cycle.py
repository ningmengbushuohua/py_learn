#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 基本使用
# a.
m = 0
while m < 5:
    print(m)
    m += 1
# 0-4

n = 0
while n < 3:
    print(n)
    n += 1
# 0-2
print("*" * 25)
# b.
m = 0
while m < 5:
    n = 0
    while n < 3:
        print(f"{m}---{n}")
        n += 1
    m += 1
# 5 * 3 =15
print("*" * 25)
# c.
m = 0
n = 0
while m < 5:
    while n < 3:
        print(f"{m}---{n}")
        n += 1
    m += 1
# 3条

'''
注意：
    a. 在执行代码中，一旦遇到循环语句，都需要把循环语句执行完，才执行后面的代码
    b. 在嵌套循环中，如果外层循环进入，内层循环需要全部执行完，才能去执行外层循环的下一次循环
'''

# 应用：打印九九乘法表
"""          
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
......

1*9=9 2*9=18 3*9=27  ......     7*9=63 8*9=72 9*9=81

规律：
    a. 行数 ：1-9
    b. 列数 ：1- 当前的行数
    c. 列 * 行 =乘积
"""
# 外层，控制行
row = 1
while row < 10:
    # 内层循环 ： 列
    col = 1
    while col <= row:
        print(f"{col} * {row} = {row * col}", end=' ')
        col += 1
    row += 1
    # 换行
    print()

for i in range(1,10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {j * i}", end=' ')
    print()


