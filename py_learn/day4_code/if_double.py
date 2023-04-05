#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
总结：
    a.if-else基本使用和if单分支的使用是相同的，条件的表示完全相同
    b.工作原理：根据条件是否成立，if分支和else分支只会有一个被执行
    c.else的后面没有条件
    d.总结：if-else实现了二选一的操作
"""

# if 双分支：
# 1.基本语法
num = 12
if num > 45:
    print("大于~~~~~~~~")
else:
    print("小于~~~~~~~~~")

# 3.应用
# a. 需求： 未成年人禁止进入网吧
age = int(int("请输入你的年龄："))
if age < 18:
    print("未成年人禁止进入网吧")
else:
    print("欢迎光临")

# b.需求2： 从控制台输入整数，判断是否是偶数
# 偶数 ：能被2 整除、 2 的倍数
# 整数/倍数 ： num1 % num2 ==0
num = int(int("请输入一个数据："))
# 注意： =： 赋值， ==:比较
if num % 2 == 0:
    print("该数是偶数")
else:
    print(f'{num}是奇数')

# c.需求3： 从控制台输入整数，判断是否是7 的倍数
num = int(int("请输入一个数据："))
if num % 7 == 0:
    print("该数是7 的倍数")
else:
    print("该数不是7 的倍数")

