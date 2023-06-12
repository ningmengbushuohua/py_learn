#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.变量的作用域的分类
num1 = 1        # G:Global,全局作用域,特点：当前py文件的任意位置都可以被访问
def outter1():
    num2 = 22   # E:Enclosing,函数作用域【外部函数中的变量】，特点：只能在外部函数中被访问
    def inner1():
        num3 = 33   # L:Local,局部作用域，特指内部函数，特点：只能在内部函数中被访问
        print('innner', num1, num2, num3)
    inner1()
    print('outter', num1, num2)
outter1()
print('global',num1)
# i o g

# 2.如果不同作用域的变量重名，变量被访问的原则： 就近原则
# 注意：虽然不同作用域中的变量重名，但相互之间没有任何关系，表示不同的变量
num = 1
def outter1():
    num = 22
    def inner1():
        num = 33
        num += 10
        print('innner', num)    # 33， 43
    inner1()
    print('outter', num)        # 22
outter1()
print('global',num)     # 11

# 3.
'''
会引入新的作用域： 函数 类  模块
不会引入新的作用域：if for while with try-except
'''
if 1:
    a = 56
print(a)

# def func():
#     bb = 19
# print(bb)
# func()
# print(bb)



