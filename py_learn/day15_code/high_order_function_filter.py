#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
filter(func,iterable):过滤

	func:函数
	iterable：可迭代对象

功能：将iterable中的元素依次传递给func,根据func的返回值决定是否保留该元素,
如果func的返回值为True,则表示当前元素需要保留，如果为False，则表示过滤


'''
# 1.已知一个列表 list1=[2,23,442,41,2,4565,25,76],挑出其中的偶数
list1=[2,23,442,41,2,4565,25,76]
def func1(x):
    if x % 2 == 0:
        return True
    return False
r1 = filter(func1, list1)
print(list(r1))

r2 = filter(lambda x:True if x % 2 == 0 else False, list1)
print(list(r2))

# 比较运算符和条件运算符符结果，是bool
r2 = filter(lambda x:x % 2 == 0, list1)
print(list(r2))
