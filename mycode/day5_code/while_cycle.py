#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
总结：
    a.while中的条件和if中的条件的使用完全相同，都可以是常量，变量或表达式
    b.在条件成立的前提下，if中的语句只会执行一次，但是，while中的语句【循环体】会执行若干次
    c.在大多数情况下，书写循环需要考虑的核心问题：控制循环的次数
      让循环可以在合适的时机停止下来，否则形成死循环
"""

# 1. while 和 if 语句的区别
'''
while 条件:
    循环体
if 条件：
    语句
'''
# print('start------')
# if 1:
#     print('hello ---if')
# print('end------')
#
# while 0:
#     print('hello ---while')
# print('end------')

# 2. while 循环的基本语法
# a. 需求： 打印十遍 hello
times = 0
while times < 10:   # 等价于n <= 9, 条件表达式
    print("hello world", times)    # 循环体
    times += 1  # 循环后的操作表达式

# 调试代码 ：debug
# 断点
print("*" * 52)
times = 0
while times < 10:   # 等价于n <= 9, 条件表达式
    times += 1  # 循环后的操作表达式
    print("hello world", times)    # 循环体

# b.
m = 9
while m >=0:
    print("hello")
    m -= 1

# c. 死循环
# 注意：常用的使用场景如果不确定循环的次数，则常用while的死循环,   结合break 使用
'''
while 真：
    循环体
注意 ：此处 表示真的条件，可以是任意数据类型的 非空数据 ，但常用 True
'''
'''
while 1:
    print('111111111')
'''
