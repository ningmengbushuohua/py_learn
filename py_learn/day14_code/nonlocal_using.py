#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# global 全局变量和局部变量直接
# nonlocal 嵌套前提下 局部作用域和函数作用域之间
# 注意：nonelocal只能使用在嵌套定义的函数中

# 1.
def outter():
    name = 'abc'    # 函数作用域
    def inner():
        # UnboundLocalError: local variable 'name' referenced before assignment
        name = '123'
        name += 'xyz'   #局部作用域， name = name + 'xyz'
        print('inner',name) # 123xyz
    inner()
    print('outter',name)    # abc
outter()

# 2.
def outter():
    name = 'abc'  # 函数作用域
    def inner():
        # UnboundLocalError: local variable 'name' referenced before assignment
        # nonlocal x: 声明x变量来自于函数作用域
        nonlocal name
        name += 'xyz'  # 局部作用域， name = name + 'xyz'
        print('inner', name)  # abcxyz
    inner()
    print('outter', name)  # abcxyz
outter()
