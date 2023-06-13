#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.装饰器执行的方式一
# def my_print():
#     print('hhhhhh~~~~~')
# def outter(func):
#     def inner():
#         print('func:', func)
#         func()
#         print('qqqqqqqqqqq~~~~~')
#     return inner
#
# f = outter(my_print)
# f()

print("*" * 90)

# 2.装饰器执行的方式二
def outter(func):
    print('outter~~~~~~start', func)
    def inner():
        print('inner~~~~~~start')
        func()      # 调用原函数
        print('qqqqqqqqqqq~~~~~')
        print('inner~~~~~~end')

    print('outter~~~~~~end')
    return inner

@outter     # 等价于 调用f = outter(my_print)，调用了outter,同时将my_print传参给func
def my_print():
    print('hhhhhh~~~~~')

print(my_print)     # <function outter.<locals>.inner at 0x000001590FB8C8B0>
my_print()  # 等价于 f()，调用innerhans

# 函数的本质是变量，函数名可以随时更改指向【重新赋值】

