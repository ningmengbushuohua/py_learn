#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1. 闭包
def outter(n):
    def inner():
        print(n)
    return inner
f = outter(66)  # 调用outter() 函数 f ---->inner
print(f)        # <function outter.<locals>.inner at 0x000001AC6E92C790>
f()     # 相当于调用inner()函数

print('*' * 50)
'''
概念：已知一个函数，如果需要给该函数增加新的功能，但是不希望修改原函数，
在Python中，这种在代码运行期间动态执行的机制被称为装饰器【Decorator】
# 装饰器：为已经存在的函数或者类添加额外的功能（python 特有）
#   本质：实际上就是一个闭包，概念：内部函数访问外部函数中的变量【函数】
'''

# 2.装饰器的基本语法
# 已知函数
def my_print():
    print('hhhhhh~~~~~')

# 装饰器
# a.定义闭包，给外部函数设置参数，参数表示需要被装饰的函数，命名：f/fun/func
def outter(func):
    def inner():
        # b.在内部函数中调用被装饰的函数，同时增加新的功能
        print('func:', func)    # func: <function my_print at 0x000002608789D820>
        func()  # 调用原函数 my_print
        print('qqqqqqqqqqq~~~~~')   #增加新功能
    return inner
# 需要装饰my_print. 所以将my_print传参给func
f = outter(my_print)    # 函数作为另外一个函数的参数，只需要传函数名，func()，表示调用
# print(f)    # <function outter.<locals>.inner at 0x000001D28A6BF280>
f() # 调用 inner()

'''
总结：
    a. outter 是装饰器的名称【外部函数的函数名】
    b.inner() 是装饰器的核心部分【调用原函数，新增新的功能】
    例如：圣诞树 = 树 + 装饰品
    c. 在inner中，新增功能还是调用原函数，理论上没有先后顺序，一般根据具体的需求决定
'''
