#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
注意：
    1.for循环主要用于遍历任何容器，比如列表，字符串，元组，字典和集合等
    2.按照顺序获取容器中的每个元素，赋值给变量名，再执行循环体，如此循环往复，直到取完容器中所有的元素为止
    3.for循环的执行次数由：容器中数据的个数  或者  容器的长度 决定
    4. len(x)  可以求容器的长度， 用于列表，字符串，元组，字典和集合等
"""

# 1.基本使用
# a.字符串
for ch in 'hellokoohggg':
    print(ch)

# b. list
for num in [23,56,56]:
    print(num+9)

# c. 元组
for num in (23,56,56):
    print(num+9)

# for _ in range(10):
#     print("hello")

for _ in 'n' * 10:
    print("hello")
# 注意：如果for 循环中定义的变量 在循环体中未被使用， 则此变量可以使用 _ 代替


# 说明：如果已知容器，则可以直接遍历，但是，如果需要for循环控制次数控制次数，一般使用range()
#  3. for + range()
# 需求： 打印100 遍 helloworld
for n1 in range(100):
    print('hello world')   # 0-99

for n1 in range(1, 100):
    print(n1)   # 1-99

for n1 in range(1, 100, 2):
    print(n1)   #1-99 之间的奇数

for n1 in range(0, 100, 2):
    print(n1)   #1-99 之间的偶数

'''
总结：
常用的使用场景
    如果不确定循环的次数，则常用while的死循环,  结合break使用
    如果确定循环的次数，则常用for,   
'''
