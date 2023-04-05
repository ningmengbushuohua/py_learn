#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1. 空列表
# 注意1：列变量的 定义 ，不要使用系统的关键字，如：int float str str list dict tuple
list1 = []
print(list, type(list1))

# 2.非空列表
# 注意2： 列表是有序的,  [索引]
list2 = [2,56,6,7,65,25]
print(list2)

# 注意3： 列表允许存储重复元素
list3 = [3,3,3,3,3,3,3]
print(list3)

# 注意4：同一列表中可以同时存储不同的数据，换句话说，列表可以存储任意的类型
list3 = [3,3,'22',True,'lp',[56,656,6]]
print(list3)

# 注意5： 列表是可变的
list3[0] = 1222
print(list3)