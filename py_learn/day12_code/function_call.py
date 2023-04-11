#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一、函数的定义
# 1.无参，无返回值
def fun1():
    print('hello，this is python fun')

# 2. 有参，无返回值
def fun2(a,b,c):
    print('hello，this is python fun')

# 3. 无参，有返回值
def fun3():
    print('hello，this is python fun')
    return 33

# 4. 有参有返回值
def fun4(a,b,c):
    print('hello，this is python fun')
    return 44

# 二、调用
# a.基本调用
# 1.无参无返回值
fun1()
# fun1(45,56) # TypeError: fun1() takes 0 positional arguments but 2 were given

# 2.有参无返回值
#fun2()  #TypeError: fun2() missing 3 required positional arguments: 'a', 'b', and 'c'
fun2(2,56,4)

# 3.无参有返回值
fun3()  # 不需要使用返回值
# r3= fun3()  # 使用返回值
# print(r3)
# print(fun3())

# 4.有参有返回值
fun4(45,56,9)
# r4 = fun4(45,56,9)
# print(r4)

# b.在函数之间的调用
def a():    # 1  5
    print('aaaa')   # 6
    b()     # 7.     14
def c():    # 2.    10
    print('ccc')    # 11
def b():    # 3.        8
    c()     # 9.    # 12
    print('bbbb')   # 13

a()     # 4.    15


# 注意：函数自己调用自己，被称为递归，但是递归是有条件的
# 恶意调用一
# def f1():
#     print('111111')
#     f1()
# f1()

# 恶意调用二
# def f1():
#     print('11111')
#     f2()
# def f2():
#     print('222222222')
#     f1()
# f1()

'''
总结：
    a.程序在执行的过程中，一旦遇到某个函数的调用，则会执行该函数的函数体
    b.当一个函数执行完毕，会返回到调用该函数的位置，代码接着向下执行       ******
'''