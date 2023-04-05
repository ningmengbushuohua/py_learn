#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# num = eval(input("输入数字"))
# temp = 10
# count = 1
# while num >= temp:
#     print(temp)
#     count += 1
#     temp *= 10
# print(f"这个数是{count}位数")


# for 循环
# temp_init = 10
# count = 0
# for temp in range(10,temp_init * 10, temp_init * 9):
#     temp_init *= 10
#     if temp_init < 12656:
#         print(temp)
#
# print(f"这个数是{count}位数")


# count = 0
# num = 3000
# while num >= 5:
#     count += 1
#     num = num // 2
# print(count)


# print("*" * 151)
# # 153
# for num in range(100, 1000):
#     num_bw = num // 100
#     num_sw = num // 10 % 10
#     num_gw = num % 10
#     if num == num_bw ** 3 + num_sw ** 3 + num_gw ** 3:
#         print(num)

#  注意：在for循环中，注意range（1,101）和 （1,101）的区别
# total = 0
# list1 =[]
# for num in range(1,100):
#     if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
#         list1.append(num)
#         total += 1
# print(total,list1)

# total = 0
# num = 1
# while num < 100:
#     if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
#         total += 1
#     num += 1
# 注意： 当while 和if嵌套是， n += 1
# print(total)

# total = 0
# for num in range(2,100,10):
#     if num % 3 == 0:
#         total += 1
# print(total)

total = 0
num = 2
while num < 100:
    if num % 3 == 0:
        total += 1
    num += 10
print(total)
