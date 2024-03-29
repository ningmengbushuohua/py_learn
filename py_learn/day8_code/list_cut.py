#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
语法：
	xx[start:end:step]
    start:开始索引，可以省略，默认为0，不省略的情况下包含在内
    end:结束索引，可以省略，默认为索引的结束【len - 1  或 -len】,不省略的情况下不包含在内
    step：表示步长，可以省略，默认为1
'''
# **********8*8
# 注意：切片之后会得到一个新的列表，对原列表没有任何影响,相当于是列表的拷贝
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
numlist = [10,20,30,40,50,60,70,80,90]
# 1. 常用
# a.
print(numlist[2:5])  # [2:5:1]      [30, 40, 50]    ***************8
print(numlist[2:8:2])   # [30,50,70]
# b.
print(numlist[:])       # [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numlist[::])      # [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numlist[::-1])    # 反转 /逆序   [90, 80, 70, 60, 50, 40, 30, 20, 10]  **********
print(numlist)

# c.
print(numlist[4:])      # [50, 60, 70, 80, 90]
print(numlist[:4])      # [10, 20, 30, 40] # 开头省略默认为0
# d. 面试题
#print(numlist[100])     # 获取元素，报错 ：IndexError
print(numlist[100:])    # 切片，不报错 ：[]
print(numlist[:100])    # 切片， 不报错 ，[10, 20, 30, 40, 50, 60, 70, 80, 90]

# 2.
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""

"""
规律1：如果start和end同正负
    第一步：计算start+step
    第二步：判断第一步计算的结果是否在给定的start和end区间内
    第三步：如果在区间内，则按照规律获取元素；如果不在区间内，则直接得结果[]
"""
print(numlist[6:1])     # []
print(numlist[6:1:-1])  # [70,60,....30]
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
print(numlist[-6:-1:-1])    # []
print(numlist[-1:-6])   # []
print(numlist[-6:-1])   # [40,50,...80]

"""
规律2：如果start和end一个为正，一个为负
    第一步：查看start的正负，索引的使用和start的正负保持一致
    第二步：如果start为正，则使用正数索引【将end的索引等价转换为正数索引】
           如果start为负，则使用负数索引【将end的索引等价转换为负数索引】
    第三步：使用规律1
"""
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
print(numlist[-6:1:-1]) # [-6:-8:-1]---->[40,30]
print(numlist[6:-1:-1]) # [6:8:-1] ---> []

# 4.
"""
规律3：如果start和end都被省略，观察step的正负
    a.如果step为正数，则从左往右进行获取【顺序获取】
    b.如果step为负数，则从右往左进行获取【倒序获取】  
"""
print(numlist[::-1])
print(numlist[::2])

# 5.
"""
规律4：列表[start::step]
    a.如果step为正数，则从左往右进行获取【顺序获取】
    b.如果step为负数，则从右往左进行获取【倒序获取】  
"""
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
print(numlist[5::-1])   #[60...10]
print(numlist[-5::1])   # [50...90]
print(numlist[:4:-1])   # []
print(numlist[0:4:-1])   # []