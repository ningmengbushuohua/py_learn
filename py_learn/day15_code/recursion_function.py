#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 函数递归
# 函数递归：函数调用自身
# 处理递归的关键：
# 	a.需要找到一个临界值【让程序停止下来的条件】
# 	b.函数相邻两次调用之间的关系


# 1.
# 恶意调用
# def a():
#     print('aaaaa')
#     a()
# a() # RecursionError: maximum recursion depth exceeded while calling a Python object

# 2.斐波那契数列
# 需求：报一个数，返回斐波那契数列中该位置的数字
"""
1   2   3   4   5   6   7   8   9   10......
1   1   2   3   5   8  13   21  34  55......

规律::
    1.func(1) = 1,func(2) = 1
    2.func(n) = func(n-1) + func(n-2)
"""
def func(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func(n-1) + func(n-2)

print(func(7)) # 13
print(func(10)) # 55
#3.求1~某个数之间所有整数的和
'''
规律; 
    a. 第一个数字是固定的 ，是1
    b.add(n) = add(n-1) + n
'''
def add(n):
    if n == 1:
        return 1
    else:
        return add(n-1) + n
print(add(100))