#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 函数 ：某些特殊功能的封装
# 【面试题】优点：
# 	a.简化代码结构，提高应用的模块性
# 	b.提高了代码的复用性
# 	c.提高了代码维护性
'''
# 冒号(:)之前函数的声明，之后函数的实现
语法：
	def  函数名(变量1，变量2....):
		    函数体
		    return   返回值
'''

# function ：功能,函数的命名常用fun\func\fn等
# 函数的定义
print('start-------')
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

print('end-----')

print(type(fun4))   # <class 'function'>

# 定义变量
name = 'abc'
# 访问变量
print(name)
print(type(name))   # <class 'str'>

'''
总结：
    1.定义函数和定义变量的本质是相同的
    2.使用函数【调用函数】和使用变量【访问变量】的本质是相同的
    3.函数的本质就是一个变量，函数名相当于变量名
    4.一个函数定义完毕，其中的函数体不会被执行，只有当函数被调用后，函数体才会执行
'''
