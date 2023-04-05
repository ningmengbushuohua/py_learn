#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    a. 逻辑判断  ，if和while
    b. 关系运算符
    c. not xx想， 不管哪种数据类型，得到的结果都是bool
    d. 表示假的数据  0  0.0  ‘’  []  {}  ()  NOne  False

'''
# 1.and 与
'''
真 and 假---》假
真 and 真----》 真
假 and 假---》假
假 and 真---》假
规律：全真为真， 有假为假
'''

'''

结论： A and B,
    如果A,是真， A and B 结果是 B 的值
    如果A,是假， A and B 结果是 A 的值,此时的B根本不参与运算，被称为短路运算
'''
# 结果是假
print(True and False)   # False
print(34 and 0)     # 0
print(23.5 and 0.0) # 0.0
print('hello' and '')   # ''
print([34,3,6] and []) # []


print(True and 'io')   # 'io'
print(34 and 10)     # 10
print(23.5 and True) # True
print('hello' and 56)   # 56
print([34,3,6] and [56]) # [56]

print('*' * 56)

print(0 and 'ss')
print(0 and [26])
print(0 and 36)
print(0 and 36.0)

print(0 and 0.0)
print(0 and 0.0)
print(0 and 0.0)
print('*' * 56)
# 2.or 或

'''
真 or 假---》真
真 or 真----》 真
假 or 假---》假
假 or 真---》真

规律：有真为真，全假为假
'''

'''
结论： A or B,
    如果A,是真， A or B 结果是 A 的值, 此时的B根本不参与运算，被称为短路运算
    如果A,是假， A or B 结果是 B 的值

'''

print(True or False)   # True
print(34 or 0)     # 34
print(23.5 or 0.0) #
print('hello' or '')   #
print([34,3,6] or []) #

print(True or 'io')   #



# 3.not 非
'''
not 真----》 假
not 假----》 真
'''
print(not 0)    # True
print(not 3)    # False
print(not '')   # True
print(not 23.5) # False



# 4.优先级
print(3 >5 and 10 < 15) # False
# 优先级 : 算术运算符 > 关系运算符 > 逻辑运算符
print(3+2 == 5 and 10 < 15 * 2) # True