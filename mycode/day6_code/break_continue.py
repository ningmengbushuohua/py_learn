#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
总结：
    a.break是一个关键字，但是可以单独作为一条语句使用
    b.如果break使用在单层循环【while和for】中，在满足条件的情况下，表示结束循环
    c.break应用在嵌套循环中，结束的是当前循环【break书写在哪个循环中，就结束哪个循环】
"""

# 1. pass :通过
# 一般用于代码块中， 为了保证程序结构的完整性，相当于是一个占位符，常位于： if for while 函数
# pass 没有实际的含义， 只是暂时用来站位 ，最终会被实际的语句所替换
# if 1:
#     pass    #占位符
# print("over")
#
# for n in range(10):
#     pass


# 注意： break 和continue 都只对循环起作用
# 2.break
# a.
n =0
while n < 10:
    print(n)
    n += 1
# 0-9
print("*******" * 20)

n = 0
while n < 10:
    print(n)
    if n == 3: # 注意： if 语句只充当条件
        break
    n += 1
# 0- 3
print("*******" * 20)
# b.
m = 0
while m < 5:
    n = 0
    while n < 3:
        print(f"{m}---{n}")
        n += 1
    m += 1
# 3 * 5 = 15
print("*******" * 20)

m = 0
while m < 5:
    n = 0
    while n < 3:
        print(f"{m}---{n}")
        if m == 1:
            break   # 结束的是内层循环 ，就近原则
        n += 1
    m += 1
# 13条 只有 1==1 1==2未被打印
print("*******" * 20)
m = 0
while m < 5:
    n = 0
    while n < 3:
        print(f"{m}---{n}")
        if n == 1:
            break   # 结束的是内层循环 ，就近原则，其他循环正常执行不受影响
        n += 1
    m += 1
print("*******" * 20)
# 10 条  所有 n=2的情况无法打印

# 3. continue
n = 0
while n < 10:
    if n == 3:
        break
    print(n)
    n += 1
print("*******" * 20)

# n = 0
# while n < 10:
#     print("start")
#     if n == 3:
#         continue  # 结束本次循环，继续下一次循环
#     print(n)
#     n += 1
# 死循环

n = 0
while n < 10:
    print("start")
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1
# 0 1 2 4 5 6 7 8 9

# 4.应用
# a.验证用户名和密码的，当用户名为 abc, 密码为123时， 则登录成功
# 否则登录失败 ，失败需要重新输入，但是只允许 错误三次

# error_num = 0
# for _ in range(3):
#     user = input("输入账号：")
#     pwd = input("输入密码")
#     if user == 'abc' and pwd == '123':
#         print('登录成功')
#         break       # 登录成功，循环可以提前结束
#     else:
#         error_num += 1
#         if error_num  == 3:
#             print('输入错误三次，禁止登录')
#             continue        # 此处使用continue 或者break 均可
#         print("用户名或者密码错误，请重新输入")

# b. 猜数字游戏
'''
从控制台输入一个数，和程序产生的随机数进行比较，范围 1- 100
根据比较结果
    输入的数 > 随机数， 提示： 你猜大了，往小的猜
    输入的数 > 随机数， 提示： 你猜小了，往大的猜
    输入的数 == 随机数， 提示： 恭喜你猜中了
如果猜中了，则表示游戏结束 ，意味着循环结束
'''
import  random
random_int = random.randint(1, 100)
guess_num = 0
while True:
    guess_num +=1
    input_num = int(input("请输入一个 1- 100 之间的数"))
    if input_num > random_int:
        print("你猜大了，往小的猜")
    elif input_num <random_int:
        print("你猜小了，往大的猜")
    else:
        print("恭喜你猜中了")
        break
print(f"你总共猜了{guess_num}次")


