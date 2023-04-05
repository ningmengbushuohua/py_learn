#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一：内置功能
# - abs(x):返回数字的绝对值
print(abs(-5))
# - max(x1,x2,…):返回给定参数的最大值
print(max(45,56,6))
# - min(x1,x2,…):返回给定参数的最小值
print(min(45,56,6))
# - pow(x,y):求x的y次方的值
print(5 ** 3)
print(pow(5, 3))
# - round(x,n):返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
print(round(52.666666666666666))
print(round(52.666666666666666, 3))
# - sum(容器)：求容器中元素的和
print(sum([2, 56, 6,656]))
print(sum(range(1, 100)))

# 二：math 模块
# - ceil(x):返回x的上入整数，不能直接访问，需要通过math访问，即math.ceil(18.1)
# - floor(x):返回x的下入整数，同ceil的用法
# - modf(x):返回x的整数部分和小数部分，两部分的数值符号与x相同，整数部分以浮点型表示，同ceil的用法
# - sqrt(x):返回数字x的平方根，数字可以为负数，返回类型为实数【浮点型】，同ceil的用法

import math
print(math.ceil(18.96))
print(math.ceil(18.16))
print(math.floor(18.16))
print(math.floor(18.96))

print(math.modf(34.16))  # (0.1599999999999966, 34.0)

print(pow(3,2))
print(math.sqrt(9)) # 3.0 算术平方根
print(9 ** 0.5)
# math.pi ：圆周率
#
# math.e ：自然常数

print(math.pi)
print(math.e)


