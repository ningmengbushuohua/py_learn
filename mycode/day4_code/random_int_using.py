#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
在Python中产生随机数的方式：
方式一：
     第一步：导入模块/导入库：import  random
     第二步：num = random.randint(start,end)，闭区间【包头包尾】,步长默认为1，无法自定义步长
方式二：
     第一步：import  random
     第二步：num = random.choice(range(start,end,step))，前闭后开区间【包头不包尾】
        range(start,end,step):相当于生成了一个容器，容器中的数据是指定的区间，指定的步长
            start：开始数字，可以省略，默认为0
            end：结束数字，不可以省略
            step：步长，可以省略，默认为1，从start~end递增，则步长为正数，从start~end递减，则步长为负数

举例：
    random.randint(0,100):获取0~100之间的任意一个整数随机数
    random.choice(range(100)):获取0~99之间的任意一个整数随机数
    random.choice(range(1,100)):获取1~99之间的任意一个整数随机数
    random.choice(range(1,100,2)):获取1~99之间的任意一个奇数随机数
    random.choice(range(0,100,2)):获取0~99之间的任意一个偶数随机数

    random.choice(range(100,2)):错误写法，说明：如果end和step未被省略，则start也不能省略
'''

# import random
# # 1.简单使用
# n1 = random.randint(0,100)
# print(n1)
#
# n2 = random.choice(range(100))  # 0~ 99, 省略开始和步长
# print(n2)
#
# n3 = random.choice(range(1, 100))   #1~ 99
# print(n3)
#
# n4 = random.choice(range(1, 100, 2))   #1~ 99 的奇数
# print(n4)
#
# n5 = random.choice(range(0, 100, 2))   #0~ 99 的偶数
# print(n5)
#
# # n6 = random.choice(range(100, 2)) # 等价与range(100, 2 , 1)
#
# print(list(range(100,2,1))) # []
# print(list(range(100,2,-1))) # [1..,99.....3]
'''
range(100,2,1)----> 100 101 102
range(100,2,-1)---->100 99 .......3
'''


# 应用
# a.在10 --80 之间获取一个数，判断是否是3的倍数
# import random   # 在实际使用中，同一个文件 只需要导入1次
# num = random.randint(10,80)
# if num % 3 == 0:
#     print(f"{num}是3的倍数")
# else:
#     print(f'{num}不是3的倍数')


# b.模拟彩票
# import  random
# ran_num = random.choice(range(1000, 10000))
# guess_num = int(input("请输入一个四位数"))
# if guess_num == ran_num:
#     print("恭喜")
# else:
#     print("谢谢参与")


# import random
# num1 = input("输入掷出骰子")
# guess_num = random.randint(1,6)
# if num1.isdigit():
#     num1 = int(num1)
#     if num1 == 1:
#         print("singing")
#     elif num1 == 2:
#         print("dancing")
#     elif num1 == 4:
#         print("dancing")
#     elif num1 == 5:
#         print("dancing")
#     else:
#         print("laughing")
# else:
#     print('输入错误')

# num1 = input("输入一个年份")
# if num1.isdigit():
#     if (int(num1) % 4 == 0 and int(num1) % 100 != 0) or (int(num1) % 400 == 0) :
#         print(f"{num1}是闰年")
#     else:
#         print(f"{num1}是平年")
# else:
#     print("输入有误")

# num1 = eval(input("请输入你的身高体重，并用逗号隔开"))
# num_high, num_weight = num1
# temp_num = num_weight / (num_high ** 2)
# if temp_num >= 18.5 and temp_num <= 24.9:
#     print("normal")
# else:
#     print("stupid")

# import  random
# num_x = random.randint(0, 99)
# num_y = random.randint(0, 199)
# if num_x > num_y:
#     print(f'x是{num_x}')
# elif num_x == num_y:
#     print(f'x+y是{num_x + num_y}')
# else:
#     print(f'y是{num_y}')

#较大的数
# num1 = eval(input("请输入三个数"))
# num_x, num_y, num_z = num1
# #方式一：
# #假设法：思路，定义一个变量max_value,    num_x 为最大值，
# max_value = num_x
# if num_y > num_x:
#     max_value = num_y
# print(f"num_x 和num_y的最大值是{max_value}")
# if num_z > max_value:
#     max_value = num_z
# print(f"num_x 、num_y和num_z的最大值是{max_value}")
#
# # 方式二：max()
# max_value = max(num_x, num_y, num_z)
# print(f"num_x 、num_y和num_z的最大值是{max_value}")


#水仙花
num1 = input("输入一个水仙花数")
if num1.isdigit() and len(num1) == 3 and num1[0] != '0':
    num1 = int(num1)
    num_hundred = num1 //  100
    num_ten = (num1 - num_hundred * 100) //  10
    num_single = num1 - num_hundred * 100 - num_ten * 10

    if num_hundred ** 3 + num_ten ** 3 + num_single ** 3 == num1:
        print("该数是水仙花数")
    else:
        print("不是水仙花数")
else:
    print("输入有误")

# 回文数
# num1 = input("输入一个五位数")
# if num1.isdigit() and len(num1) == 5:
#     for i in range(0,4):
#         if(num1[i] == num1[4-i]):
#             print("是回文数")
#         else:
#             print("不是回文数")
# else:
#     print("输入有误")