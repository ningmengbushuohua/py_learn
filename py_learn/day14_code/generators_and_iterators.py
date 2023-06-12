#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
可迭代对象：Iterable,可以直接作用于for循环的对象【可以使用for循环遍历其中元素的对象】，
    如：list,tuple,dict,set，str,range(),生成器等
迭代器:Iterator,可以直接作用于for循环,或者可以通过next()获取下一个元素的对象，
    如：生成器
'''

# 1. 列表
list1 = [i ** 2 for i in range(100)]
print(list1)

# 2.生成器
# a.方式一
gen1 = (i ** 2 for i in range(100))
print(gen1)     #<generator object <genexpr> at 0x0000016879F71890>
print(type(gen1))        # <class 'generator'>

# b.方式二,函数生成器
# def func():
#     return 10
# r1 = func()
# print(r1)

# 预定义
def func():
    yield 'hhhhhh'
r1 = func()
print(r1)       # <generator object func at 0x000002BCD9D119E0>

def func2():
    yield 10
    yield 1055
    yield 1011
r2 = func2()
print(r2)

def func3():
    for i in range(100):
        yield i ** 2
r3 = func3()
print(r3)


# 3.获取生成器中的元素
# 注意：生成器的本质还是一个容器，所以仍然可以使用for循环
# 方式一：next()
n1 = next(r1)
print(n1)
# n1 = next(r1)       # StopIteration: 停止迭代
# print(n1)

# m1 =next(r2)
# print(m1)
# m2 =next(r2)
# print(m2)
# m3 =next(r2)
# print(m3)
# m4 =next(r2)    # StopIteration
# print(m4)

# 方式二：for()
# for n in r2:
#     print(n)
# m4 =next(r2)    # StopIteration
# print(m4)
'''
10 
1055 
1011
---
'''

# 列表推导式，
# 字典推导式
# iterable: 可迭代对象
# iterator: 迭代器
# geneator: 生成器