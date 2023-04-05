#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if 单分支

"""
总结：
    a.在Python中，是通过缩进区分代码块的，在编写程序的过程中，要注意缩进对齐问题,
      一个缩进一般是4个空格或一个tab键
    b.if语句中的条件是常量，变量或表达式
    c.Python中表示假的数据：0  0.0   False "" []  ()  {}  None等
    d.if单分支的工作原理：如果条件成立，则执行代码块中的语句，
      如果条件不成立，则整个if语句会被跳过，继续执行后面的代码
    e.总结：代码块要么执行，要么不执行
"""

#  1.基本语法
print('sssssssssssssss')
if False:
    print('okkkkkkkkkk')
print('xxxxxxx')

# 2.

# a. 用数据直接作为条件
if 'hhhh':
    print('hhhhhhhh')

# b.用变量作为条件     ************
num = 0
if num:
    print('ooooooooooo---2222')

# c. 用运算符       ***************
# 主要包括： 条件 ，逻辑 成员
num1 = 2
num2 = 56
if num1 == num2 and num1 < num2: # or 有真为真
    print('sssss---3')


# 3.应用
# a. 需求： 未成年人禁止进入网吧
age = int(int("请输入你的年龄："))
if age < 18:
    print("未成年人禁止进入网吧")

# b.需求2： 从控制台输入整数，判断是否是偶数
# 偶数 ：能被2 整除、 2 的倍数
# 整数/倍数 ： num1 % num2 ==0
num = int(int("请输入一个数据："))
# 注意： =： 赋值， ==:比较
if num % 2 == 0:
    print("该数是整数")

# c.需求3： 从控制台输入整数，判断是否是7 的倍数
num = int(int("请输入一个数据："))
if num % 7 == 0:
    print("该数是7 的倍数")
