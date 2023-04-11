#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.必需参数
# 注意：必须参数必须传参，一定要注意实参和形参的数量相同
def a1():
    print('aaa----111')
a1()

def a2(num1, num2):
    print('aaa----222',num1, num2)
a2(45, 6)

# 需求：求一个数和5 的和
def a3(a,b):
    print(a + b)
a3(34,5)
a3(56,5)
a3(78,5)
a3(2,5)

# 2.默认参数
# 注意：默认参数体现在形参上，表示形参有默认值,默认参数的好处：简化函数的调用
def b1(a, b=5):
    print(a + b)
b1(34)
b1(56)
b1(78)
b1(2)
b1(89, 56)


def b2(a=2,b=5):
    print(a + b)
b2()
b2(3)
b2(2,2)

# 部分默认参数，默认参数往后写
# 错误的写法
# SyntaxError: non-default argument follows default argument
# def b3(a=2,b):
#     print(a + b)

# 默认参数常见于系统函数
# print(34,56,8)    # sep=' ',  end='\n'
# print(34,56,8, sep='@')
# range(10)  #  start=0  step =1

# 3.关键字参数
# 注意： 关键字参数体现在实参上
def c1(name,age):
    print(f"姓名{name}，年龄{age}")
c1('张三', 48)
# c1(18,'张三')

# 关键字参数的写法：函数名(变量名 = 值)，此处的变量名一定要和形参的变量名一致
c1(age=18, name='张三')
# c1(age=18, name1='张三')  # TypeError: c1() got an unexpected keyword argument 'name1'

def c2(name,age=0):
    print(f"姓名{name}，年龄{age}")
c2('李四')
c2('李四', 78)
c2(name='李四')
c2(name='李四', age=10)
c2(age=10, name='李四' )
# 必须参数写在前面
c2('李四', age=10)
# 错误写法
# c2(age=8)   # TypeError: c2() missing 1 required positional argument: 'name'
# c2(name='李四', 10)   # SyntaxError: positional argument follows keyword argument

# 关键字参数在系统函数中的体现
# print(34,56,8, sep='@')


# 4. 不定长参数【可变参数】
# 注意：实参可以书写若干个
# a. *x: x被当做元组来处理，实参可以传递无数个
def d1(*num):   # 打包
    print(num)
    print(num[0])
d1(5,56,66,3,89,9,9,7)
# d1()
d1(45)

# b. **x, x被当做字典来处理，实参可以传递无数对键值对
def d2(**num):
    print(num)
d2()
# 注意：实参的形式，key=value 的形式,【相当于定义变量的书写形式】
d2(h=5, j = 6,k =56)


# 注意1: 在同一个函数中，同种符号只能出现一次
# 错误的写法
# def d3(*num1, *num2):
#     print(num1,num2)
#
# def d3(**num1, **num2):
#     print(num1,num2)

# 注意2： * 和** 可以同时出现,后期在使用的时候，经常写成 *args, **kwargs
def d3(*num1, **num2):
    print(num1,num2)
d3(56,56,9)
d3(56,56,9,a=3,b=5)
d3(a=3,b=5)