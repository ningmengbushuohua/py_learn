#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1. 基本语法
# 不常用： 当循环没有break, 循环语句执行完毕后， else代码块都会执行，意义不大
m = 0
while m < 5:
    print(m)
    m += 1
else:
    print("else-----111")

for n in range(5):
    print(n)
else:
    print("else----222")
print("****" * 23)
# 2.常用： 结合break     *******
# 如果break被执行 ，则循环的else 不会执行
# 如果break 不会被执行， 则循环的else正常执行
m = 0
while m < 5:
    print(m)
    if m > 20:
        break
    m += 1
else:
    print("else-----111")

# 3.应用
# a.验证用户名和密码的，当用户名为 abc, 密码为123时， 则登录成功
# 否则登录失败 ，失败需要重新输入，但是只允许 错误三次

for i in range(3):
    user = input("输入账号：")
    pwd = input("输入密码")
    if user == 'abc' and pwd == '123':
        print("登录成功")
        break
    else:
        if i == 2:
            continue    #结束本次循环
        print("用户名或者密码有误，请重新输入：")
else:
    print("输入错误三次，禁止登录")
