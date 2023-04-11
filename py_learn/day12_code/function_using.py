#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.需求：打印十遍 九九乘法表
def myprint():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}*{i}={i * j}", end=' ')
        print()
for _ in range(10):
    myprint()

# 2.需求：打印指定行数的九九乘法表
def myprint2(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(f"{j}*{i}={i * j}", end=' ')
        print()
myprint2(3)
myprint2(9)
# 3.需求：判断一个数是否是偶数
#
def iseven(num):
    if num % 2 == 0:
        print(f"{num}是偶数")
    else:
        print(f"{num}是奇数")
iseven(56)
iseven(25)
iseven(89)