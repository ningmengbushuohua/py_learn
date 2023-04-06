#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一：增
# 1.    ************
d1 = {"a":10, 'b':20}
d1['c'] = 30
print(d1)

# 2.update():更新，合并
# d1.update(d2) :将d2中的键值对合并到d1中
d1 = {"a":10, 'b':20}
d2 = {"an":10, 'bc':20, 'b':60}
d1.update(d2)
print(d1)

d2.update(d1)
print(d2)

# 二、删
# 1.pop()：通过指定的key,删除key-value对     ******************
d1 = {'a': 10, 'b': 60, 'an': 10, 'bc': 20}
d1.pop('an')
print(d1)
# d1.pop('d')     # KeyError: 'd'

# 2.clear():清空字典
d1.clear()
print(d1)


# 3.del 字典[key]
d1 = {'a': 10, 'b': 60, 'an': 10, 'bc': 20}
del d1['a']
print(d1)

# 三、改
# 字典中没有提供修改的功能

# 四。查
print(len(d1))
print(d1.keys())
print(d1.values())
print(d1.items())

# 五、其他
'''
注意：
    可变的数据类型，都有copy()的功能
    不可变的数据类型，没有copy()
    字典和列表相似，同样可以使用 copy(),copy.copy(),copy.copy()
    字典和列表一样，都遵循深浅拷贝的使用规则
'''
d1 = {'a': 10, 'b': 60, 'bc': 20}
d2 = d1.copy()
d1['a'] = 65
print(d2)   # {'a': 10, 'b': 60, 'bc': 20}

import copy
d3 = {'ass':56, 'oo': 45, 'm':[1,56,4]}
d4 = copy.deepcopy(d3)      # 深拷贝成新的 dict
d3['m'][-1] = 88
print(d3)       # {'ass': 56, 'oo': 45, 'm': [1, 56, 88]}
print(d4)       # {'ass': 56, 'oo': 45, 'm': [1, 56, 4]}

d3 = {'ass':56, 'oo': 45, 'm':[1,56,4]}
d4 = copy.copy(d3)      #d3.copy()  浅拷贝 只拷贝最外层，里层多个数据共用一个
d3['m'][-1] = 88
print(d3)       # {'ass': 56, 'oo': 45, 'm': [1, 56, 88]}
print(d4)       # {'ass': 56, 'oo': 45, 'm': [1, 56, 88]}
