#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数：如果A函数作为B函数的参数，B函数调用完成之后，得到一个结果，则B函数被称为高阶函数
# 例如：map(),reduce().filter(),sorted()

'''
map:映射
map(func,iterable)，返回值是一个iterator【容器，迭代器】
   func:函数
   iterable：可迭代对象【容器】，可以是多个，常用列表

功能：将iterable容器中的每一个元素传递给func,func返回一个结果，结果会成为iterator中的元素
 容器----》func----》新的容器

'''
# 1. 生成一个容器，其中的元素是 1,4,9,16
# a.
list1 = [n ** 2 for n in range(1,6)]
print(list1)

# b.
r1 = (n ** 2 for n in range(1,6))
print(r1)
# for next ,转为列表
print(list(r1))

# c.
def fun11(x):
    return x ** 2
r11 = map(fun11, range(1, 6))
print(r11)
print(list(r11))

# d.        ************************
r12 = map(lambda x:x ** 2, range(1, 6))
print(r12)
print(list(r12))

# 2.
'''
注意: 
a. map 中的func函数需要设置几个参，取决于有几个iterable 参与运算
工作原理:将多个iterable 相同位置的元素同时传参给func
'''
def fun2(a,b):
    return a + b
r21 = map(fun2, [1,5,3,3,55], [3,1,2])
print(list(r21))

r22 = map(lambda a, b : a + b, [1,5,3,3,55], [3,1,2])
print(list(r22))

# pandas