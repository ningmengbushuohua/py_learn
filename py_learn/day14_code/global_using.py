#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.
a = 1
def func():
    a = 2
func()
print(a)    ## 1

# 2.[面试题]
'''
a = 1
def func():
    # UnboundLocalError: local variable 'a' referenced before assignment
    a += 2  
    a = a + 2
func()
print(a)
'''
'''
错误原因 ：
    1. a += 2 等价于a = a + 2
    2.在进行=运算时，永远先计算=右边，将= 右边的计算结果赋值给= 左边的变量
    3.虽然不同作用域中的变量重名，但相互之间没有任何关系，表示不同的变量
    
    综上所述，a +2 中的a 和a = 1 中的a是两个不同的变量，所以 a + 2 中的a未被定义则使用了
'''

# 解决方案一：表示不同的变量
a = 1
def func():
    a = 3
    a = a + 2
    print('内部',a)   # 5
func()
print('外部', a)    # 1

# 解决方案二：表示同一个的变量
a = 1
def func():
    # global x:声明函数中使用的x来自于全局变量
    # a = 7  # SyntaxError: name 'a' is assigned to before global declaration
    # global a
    global  a
    a = a + 2
    print('内部',a)   # 3
func()
print('外部', a)    # 3
