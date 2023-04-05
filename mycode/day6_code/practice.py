#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a = sum(range(1, 101, 2))
b = sum(range(0, 101, 2))
print(a - b)

total = 1
for index in range(1, 16):
    total *= index
print(total)
#
# height = 0.08 / 1000
# count = 0
# while True:
#     if height <= 8848.13:
#         height *= 2
#         count += 1
#     else:
#         break
# print(count)

# 质数，只能被1 和 它本身整除的数， 最小的质数是 2
# 判断一个数是否是质数
num = 20
# 方式一： 假设法
# 思路： 只要在 2- num-1  之间找到一个数，能够整除num,则说明 num 不是质数
result = True
for n in range(2, num):
    if num % n == 0:
        result = False
        break
if result:
    print(f"{num}是质数")
else:
    print(f"{num}不是质数")

# 方式二 ：统计个数
count = 0
for n in range(1, num + 1):     #range(2, num)
    if num % n == 0:
        count += 1
if count == 2:      # count == 0
    print(f"{num}是质数")
else:
    print(f"{num}不是质数")

# 方式三: for --else
num = 17
if num < 2:
    print(f"{num} 不是质数")
else:
    for n in range(2, num):
        if num % n == 0:
            print(f'{num} 不是质数')
            break
    else:
        print(f"{num} 是质数")

# list_zhishu = []
# count = 0
# for i in range(101, 200):
#     for k in range(2, i):
#         if i % k == 0:
#             break
#     else:
#         list_zhishu.append(i)
#         count += 1
# print(count)
# print(list_zhishu)
# 21
# [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

'''
1
12
123
1234
....
123456789
'''
# for i in range(1, 10):
#     for k in range(1, 10):
#         if k > i:
#             break
#         print(k, end='')
#     print()

# for i in range(1, 10):
#     for k in range(1, i + 1):
#         print(k, end='')
#     print()



# while True:
#     input_str = input("请输入信息")
#     if input_str == '0':
#         break
#此处想的过于简单... 无法判断立刻从键盘读取的字符


# 阶乘分之一 相加
# total = 1
# for index in range(1, 16):
#     total *= index

# total = 0
# for i in range(1, 21):
# 求分母的阶乘
#     num_index = 1
#     for k in range(1, i+1):
#         num_index *= k
# 求和
#     num_index = 1 /num_index
#     total += num_index
# print(total)

# 阶乘：方式 二：
fac = 1
total = 0
for n in range(1,21):
    fac *= n
    total += 1 / fac
print(total)


# for i in range(3):
#     username = input("请输入用户名")
#     pwd = input("请输入密码")
#     if username == 'admin' and pwd == 'abc123':
#         print("登录成功")
#         break
#     else:
#         if i == 2:
#             continue
#         print("用户名或者密码输入")
# else:
#     print("三次输入错误，禁止登录")

# 1  123  4   567    (4i+1)
# 2  12  345  67
# 3  1   23456 7
# 4  1234567

# 0  012  3 456     3-0, 4+i
# 1  01  234 56     3-1,4+1
# 2  0  12345 6     3-2,4+2
# 3  123456         3-3,4+3

# for i in range(0, 4):
#     for k in range(0, 7):
#         if k >=3-i and k < 4 + i:
#             print('*', end='')
#         else:
#             print(' ',end='')
#     print()

# 0  0123456
# 1  0 12345 6
# 2  01 124 56  0,2  7-2,7
# 3  012 3 456  0,3  7-3,7


for i in range(0, 4):
    for k in range(0, 7):
        if (k >=0 and k < i) or (k >= 7-i and k < 7):
            print(' ', end='')
        else:
            print('*',end='')
    print()


# for i in range(1, 101):
#     for j in range(1,100):
#         for k in range(1,99):
#             if 3 * i + 2 * j + 0.5 * k == 100 and i + j + k == 100:
#                 print(f"大马{i},中马{j},小马{k}")

'''
2 30 68
5 25 70
8 20 72
11 15 74
14 10 76
17 5 78
'''