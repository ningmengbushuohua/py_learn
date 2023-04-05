#!/usr/bin/env python3
# -*- coding: utf-8 -*-
products = [["iphone",6888],["MacPro",14800],
            ["小米6",2499],["Coffee",31],
            ["Book",60],["Nike",699]]

# 1. 基本语法
print(products[0])
print(products[0][0])

print(products[-1])
print(products[-1][-1])

# 2.二维列表的遍历
# a.
for sublist in products:
    for ele in sublist:
        print(ele)

numlist = [1,2,[3,4]]
for ele in numlist:
    if type(ele) == list:
        for num in ele:
            print(num)
    else:
        print(ele)

# b.
products = [["iphone",6888],["MacPro",14800],
            ["小米6",2499],["Coffee",31],
            ["Book",60],["Nike",699]]
for i in range(len(products)):
    #print(i,products[i])
    for j in range(len(products[i])):
        print(j,products[i][j])