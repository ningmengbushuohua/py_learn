#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}是闰年")
    else:
        print(f"{year}是平年")

'''
31: 1 3 5  7 8 10 12
30:4 6 9 11
2 :
'''


def every_month_day_num(month, is_leap_year=True):
    if month in [1,3,5,7,8,10,12]:
        print(f"{month}月有31天")
    elif month == 2:
        if is_leap_year:
            print(f"{month}月有29天")
        else:
            print(f"{month}月有28天")
    else:
        print(f"{month}月有30天")

def is_which_season(month):
    if month in [3,4,5]:
        print('春天')
    elif month in [6,7,8]:
        print('夏天')
    elif month in [9,10,11]:
        print('秋天')
    else:
        print('冬天')

def is_prime_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0 :
                print(f"{num}不是质数")
                break
        else:
            print(f"{num}是质数")

is_prime_num(10)

def huiwenshu(num):
    num_str = str(num)
    num_str_list = [ch for ch in num_str]
    num_str_list.reverse()
    num_str1 = "".join(num_str_list)
    num_new = int(num_str1)
    if num_new == num:
        print(f"{num}是回文数")
    else:
        print(f"{num}不是回文数")
huiwenshu(122)

def max_and_avarge(*num):
    print(f"最大值是{max(num)}")
    print(f"平均值是{sum(num) / len(num)}")
max_and_avarge(15,56,89,8)

def max_and_count(*num):
    print(f"平均值是{sum(num) / len(num)}")
    avarge = sum(num) / len(num)
    count = 0
    for i in num:
        if i > avarge:
            count += 1
    print(f"高于平均数的值个数是{count}")
max_and_count(15,56,89,8)

def narcissus_num(num):
    num_bai = num // 100
    num_shi = (num // 10) - (num_bai * 10)
    num_ge = num % 10
    if num_shi ** 3 + num_ge ** 3 + num_bai ** 3 == num:
        print(f'{num}是水仙花数')
    else:
        print(f'{num}不是水仙花数')

narcissus_num(153)
narcissus_num(371)