#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = 2
y = 3

# temp = x
# x = y
# y = temp

# x = x + y
# y = x - y
# x = x -y

x,y = y,x

def reverse_str(str1):
    re = ''
    list1 = list(str1)
    #list1.reverse()
    list1 = list1[::-1]
    for i in list1:
        re += i
    return re
# print(reverse_str("que"))

# str1 = 'que'
# ree = ''
# for i in range(len(str1) -1, -1, -1):
#     ree += str1[i]
# print(ree)

'''
11.编写程序，找到下面字典中年龄最大的人，并输出
persons = {“li":18,"wang":50,"zhang":20,"sun":22}
'''
# persons = {"li":18,"wang":50,"zhang":20,"sun":22}
# max_age = 0
# person_max_age = ''
# for k,v in persons.items():
#     if v >= max_age:
#         max_age = v
#         person_max_age =k
# print(person_max_age)

persons = {"li":18,"wang":50,"zhang":20,"sun":22}
# 方式一:
max_values = max(persons.values())
max_age_persons = []
for k,v in persons.items():
    if v == max_values:
        max_age_persons.append(k)
print(f'最大的年龄，{max_values},都有{max_age_persons}')

# 方式二：max(iterable),如果是字典求的是所有key的最大值，
max_age_person = max(persons,key=lambda x:persons[x])
print(max_age_person, persons[max_age_person])

# 字符串练习 1
def count_letter(str1):
    dict1 = {s : str1.count(s) for s in str1}
    count = 0
    letter = ''
    for k,v in dict1.items():
        if v >= count:
            count = v
            letter = k
    return letter
print(count_letter('nfiwsrfhweusdasd'))

import string
import random
def generator_code(length):
    code = ''
    for _ in  range(length):
        code += random.choice(string.digits)
    return code
print(generator_code(5))