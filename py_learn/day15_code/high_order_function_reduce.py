#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

reduce(func,seq)
	func:函数
	seq:序列【容器】
功能：减少

首先将seq中的第0个元素和第1个元素传递给func,进行运算，返回结果1
接着，将 结果1 和第2个元素传递给func,进行运算，返回结果2
接着，将 结果2 和第3个元素传递给func,进行运算，返回结果3
....
直到所有的元素全部参与运算，表示运算结束

注意:
    a.func 函数需要设置两个参数
    b.表示数量的减少
    c.区别于map, reduce在使用之前一定需要先导入
'''
import functools
# 1.求1~100 之间所有整数的和
# a.sum()
# b. for/while
# c.
def func1(a,b):
    # print(a,b)
    return a + b
r11 = functools.reduce(func1,range(1,101))
print(r11)

# d.        *********
r12 = functools.reduce(lambda x,y: x+y,range(1,101))
print(r12)

# 求15的阶乘
r13 = functools.reduce(lambda x,y: x*y,range(1,16))
print(r13)