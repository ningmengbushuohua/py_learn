#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 需求：书写一个装饰器，同时装饰多个函数，给多个函数同时增加一个新的功能
# 注意：如果同一个装饰器装饰多个不同的函数，为了适配所有的函数，
# 则给装饰器的内部函数设置不定长参数 *args, **kwargs
def outter(func):
    def inner(*args, **kwargs): # *args, 元组； **kwargs, 字典
        print(args) # 打包，元组
        func(*args, **kwargs)      # 拆包，调用原函数,注意传参问题
        print('qqqqqqqqqqq~~~~~')
    return inner

@outter  #调用outter
def a():
    print('aaaa')
@outter
def b(n1,n2):
    print('bbbb', n1,n2)
@outter
def c(x,y,z):
    print('cccc', x,y,z)

# 调用inner
a()
b(34,78)
c(43,23,2)

# 2.【面试题】 书写一个装饰器，可以统计任意一个函数的执行时间
import time
print(time.time())  # 获取从1970.1.1 00:00：00 开始的时间戳【秒数】
def wrapper(func):
    def get_time(*args, **kwargs):
        time1 = time.time()     # 开始时间戳
        func(*args,**kwargs)
        time2 = time.time()     # 结束时间戳
        return  round(time2 - time1, 3)
    return get_time
@wrapper
def check():
    for n in range(500000):
        pass
r2 = check()
print('花费的时间', r2)
