#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.函数本质是一个变量，函数名其实就是一个变量名
#
r1 = abs(-30)   # 调用函数
print(r1)   # 获取函数的返回值 ，30
print(abs)  # 函数本身，<built-in 内置 function abs>

f1 = abs
print(f1(-26))

# 注意，自定义变量的时候，一定要避免和系统的函数重名，否则会导致系统函数的失效
abs = 'abx' # 变量可以重新赋值
print(abs)
# print(abs(-50))     # TypeError: 'str' object is not callable

# 2.一个函数可以作为另一个函数的参数或返回值使用,只需要传递或返回函数名即可
def add(a,b,f):
    print(f(a) + f(b))
# add(45,5,89)    # TypeError: 'int' object is not callable
add(-45,-7,abs)