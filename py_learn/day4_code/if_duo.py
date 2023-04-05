#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注意：
    a.如果需要操作的情况在3种及3种以上，则使用if多分支
    b.if-elif...-else实现的是多选一的操作
    c.不管多分支中有多少个条件成立，都只会执行其中的一个分支,哪个分支在最前面则执行哪个分支
    d.else分支可以省略，但是，一般情况下，如果if和elif对应的所有的条件都不满足，则会执行else分支
    e.if和elif的后面都需要添加条件，else的后面一定不要添加条件
"""

# 1.基本语法
# a. if~~elif~~elif```
# num = int(input("请输入一个数字"))
# print('start------')
# if num == 1:
#     print('a')
# elif num == 2:
#     print('b')
# elif num == 3:
#     print('c')
# elif num == 4:
#     print('d')
# elif num == 5:
#     print('f')
# print('end------')

# a. if~~elif~~elif```else
num = int(input("请输入一个数字"))
print('start------')
if num == 1:
    print('a')
elif num == 1:
    print('b')
elif num == 1:
    print('c')
elif num == 4:
    print('d')
elif num == 5:
    print('f')
else:
    print('hhhhhhhhhhh')
print('end------')

# 2.应用
# 需求：从控制台两个数，比较大小
# num1 = int(input("请输入第一个数"))
# num2 = int(input("请输入第二个数"))
# if num1 > num2:
#     print("大于")
# elif num1 < num2:
#     print('小于')
# else:
#     print('等于')

# 方式二：扩展 ：eval(xx), 识别xx字符串中的代码并执行
r= eval(input("请输入连个数，并用逗号隔开"))
print(r, type(r))
num1, num2 = eval(input("请输入连个数，并用逗号隔开"))
print(type(num1), type(num2))
if num1 > num2:
    print("大于")
elif num1 < num2:
    print('小于')
else:
    print('等于')

