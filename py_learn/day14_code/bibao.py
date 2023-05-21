#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 闭包 ：如果两个函数嵌套定义，如果在内部函数中访问了外部函数中的变量，则构成了一个闭包
# 外部函数和内部函数都可以有参数和返回值
# 1.
def func1():
    num1 = 50
    def func2():
        num2 = 500
        total  = num1 + num2
        print(total)
    return func2
f2 = func1()
print(f2)
f2()

# 2.
def func1(a,b):
    num1 = 50
    def func2():
        num2 = 500
        total  = num1 + num2
        print(total,a,b)
    return func2
f2 = func1(12,56)
f2()

# 3.
def func1(a,b):
    num1 = 50
    def func2(x,y,z):
        num2 = 500
        total  = num1 + num2
        print(total,a,b,x,y,z)
    return func2
f2 = func1(12,56)
f2(1,2,3)   # 此处调用f2,相当于调用func2，所以需要和func2的参数保持一致


# 4.
def func1(a,b):
    num1 = 50
    def func2(x,y,z):
        num2 = 500
        total  = num1 + num2
        print(total,a,b,x,y,z)
        return 'abc'
    return func2
f2 = func1(12,56)
abc = f2(1,2,3)
print(abc)      # abc