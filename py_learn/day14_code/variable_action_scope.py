#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.变量的作用域的分类
num1 = 1        # G:Global,全局作用域,特点：当前py文件的任意位置都可以被访问
def outter():
    num2 = 22   # E:Enclosing,函数作用域【外部函数中的变量】，特点：只能在外部函数中被访问
    def inner():
        num3 = 33   # L:Local,局部作用域，特指内部函数，特点：只能在内部函数中被访问
        print('innner', num1, num2, num3)
    print('outter', num1, num2)