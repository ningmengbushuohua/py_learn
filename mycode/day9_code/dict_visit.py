#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#1. 通过键访问值
dict1 = {"小明":88, 'age':18, '阿哥':18}
print(dict1)

# a.字典[key]: 只能获取存在的key 对应的value
print(dict1['age'])
# print(dict1['weight'])      # KeyError: 'weight'

# b. 字典.get(key) ：如果key不存在 ，返回None       *****
print(dict1.get('age'))
print(dict1.get('weight'))  # None

# 2.通过键访问值，然后修改值
# 语法： 字典[key] = 新值
dict1 = {"小明":88, 'age':18, '阿哥':18}
print(dict1)

# a. key 如果存在，则 字典[key] = 新值， 表示修改字典中的指定键对应的 值
dict1['小明'] = 9
print(dict1)        # {'小明': 9, 'age': 18, '阿哥': 18}

# b. key 如果不存在，则 字典[key] = 新值，  表示向 字典中 添加一对键值对
dict1['狗子'] = 173
print(dict1)        # {'小明': 9, 'age': 18, '阿哥': 18, '狗子': 173}

# dict1.get('狗大') = 173     修改值不能使用 get()



