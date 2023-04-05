#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字典中可以存储任意类型的数据
# 键唯一
# 键可以使用数字、布尔值、元组，字符串等不可变数据类型，但是一般习惯使用字符串，切记不能使用列表等可变数据类型,但是，值的数据类型没有限制

# 1.  {key1:value1,key2:value2....}
dict1 = {'name':'张三','age':18}
print(dict1)
print(type(dict1))

# 2. 字典[key]=value      ************
dict2 = {}
dict2['aa'] = 18
dict2['bb'] = 19
print(dict2)

# 3.dict(key1=value1,key2=value2....)
# 注意：书写方式类似 变量的定义，最终变量名将充当字典中的键
dict3 = dict(name='坤坤', hobby='篮球')
print(dict3)

dict31 = {3:'简介', 56:'所示'}
print(dict31)

# 错误写法： SyntaxError
# dict32 = dict(10='a', 20='b')
# print(dict32)

# 4.dict([(key1,value1),(key2,value2)....])     *********
# 键值对可以有很多对，列表，可以新加键值对。一个键值对两个数据，用元组，不能增加
dict41 =dict([('name','坤坤'),('hobby','篮球')])
print(dict41)


dict41 =dict([['name','坤坤'],['hobby','篮球']])    # 列表可变，不建议使用
print(dict41)

dict41 =dict((('name','坤坤'),('hobby','篮球')))
print(dict41)


# 5.dict(zip([key1,key2......],[value1,value2.......]))     **********
# zip :映射
dict51 = dict(zip(['a','b','c'],[12.56,89,89]))
print(dict51)

dict51 = dict(zip(('a','b','c'),(12.56,89,89)))
print(dict51)

dict51 = dict(zip(['a','b','c'],[12.56,89,89,89,98,9,7]))
print(dict51)
dict51 = dict(zip(['a','b','c','d','f'],[12.56,89,89]))
print(dict51)