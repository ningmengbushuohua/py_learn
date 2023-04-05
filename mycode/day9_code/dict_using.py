#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. {}
# 字典
d1 ={'a':10, 'b':20}
print(type(d1))     # <class 'dict'>

# 集合
d2 = {34,56,6}
print(type(d2))     # <class 'set'>

# 注意： {}为空时， 默认表示为 字典
d3 = {}     # 空字典
print(type(d3))     # <class 'dict'>

d4 = set()   # 空集合
print(type(d4))

# 2.键值是否可以重复
# a.键是唯一 的
# 注意：每个字典中的key是惟一的 。如果出现多个相同的key,后面的value会覆盖之前的value
dict1 = {"name":'小明', 'age':18, 'name':"zzz"}
print(dict1)        # {'name': 'zzz', 'age': 18}

# b.值是可以重复的，
dict1 = {"小明":88, 'age':18, '阿哥':18}
print(dict1)    # {'小明': 88, 'age': 18, '阿哥': 18}

# 3. 键值的数据类型：
# a.键只能是不可变的数据类型
d1 = {10:24, 34.5:50,'abc':56,True:59, (45,56):'ss'}
print(d1)
# 错误写法
# d2 = {[56,6,7]: 'abn'}        # TypeError: unhashable type: 'list'
# print(d2)

# b.值可以是任意的类型

# 4. 字典是无序的
'''
有序的数据【索引】： 列表  字符串  元组
无序的数据  ：字典 集合
'''
'''
字典 的本质是无序的，在python3.7 之前，打印字典输出的结果是无序的
                在python3.7 之后，打印字典输出的结果看起来是有序的
'''
s1 = {23,56,7,8,2}
print(s1)