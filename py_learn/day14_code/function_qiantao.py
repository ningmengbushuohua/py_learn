#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 函数的嵌套定义
# 1. 在func2中访问func1中的变量，求num1和num2的和
# 错误的写法
# def func1():
#     num1 = 50
# def func2():
#     num2 = 50

# 正确的写法1:返回值
# def func1():
#     num1 = 50
#     return num1
# def func2():
#     num2 = 500
#     total = func1() + num2
#     print (total)
# func2()


# 正确的写法2：函数的嵌套定义
# def func1():
#     print('11111111---start')
#     num1 = 50
#     def func2():
#         print('22222---start')
#         num2 = 500
#         total  = num1 + num2
#         print(total)
#     print('111111111111----end')
# func1()
# # func2()     # NameError: name 'func2' is not defined

# 2.嵌套定义的函数如何调用
# a. 方案1： 直接在func1函数内部直接调用func2
# def func1():
#     print('11111111---start')
#     num1 = 50
#     def func2():
#         print('22222---start')
#         num2 = 500
#         total  = num1 + num2
#         print(total)
#     func2()
#     print('111111111111----end')
# func1()

# b.方案2： 将func2设置为func1的返回值，后期常用，常用于装饰器
def func1():
    print('11111111---start')
    num1 = 50
    def func2():
        print('22222---start')
        num2 = 500
        total  = num1 + num2
        print(total)
    print('111111111111----end')
    # 注意：函数A作为函数B的参数或者返回值，只需要使用函数名即可，
    # 函数名表示函数本身
    # return func2() TypeError: 'NoneType' object is not callable
    # 原因 func2()表示调用，返回值None，无法返回
    return func2


f2 = func1()    #地址
print(f2)       # <function func1.<locals>.func2 at 0x000001E931BFC790>

# 调用f2,相当于调用func2
f2()