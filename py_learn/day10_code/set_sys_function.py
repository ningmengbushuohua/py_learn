#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 集合可变的，和list、dict相似

# 字典的key, 不可变的数据类型， TypeError: unhashable type
# 一：增
# 1.add(x) x:不可变的数据类型
s1 = {1,2,3,4}
s1.add(44)
print(s1)

s1.add(44.5)
print(s1)

s1.add(False)
print(s1)

s1.add('abc')
print(s1)

s1.add((56,6,7))
print(s1)
# 注意，集合中相当于存储了字典中的一组key,通过add进行添加元素，只能添加不可变的数据类型
# s1.add([23])
# print(s1)



# 2.update(x): x 只能是可迭代对象 【容器】，表示将x中的元素合并到集合中
# 打碎加入，不要容器，只要其中的数据
# 字符串、列表、字典、 元组、range()
s1 = {11,55,22}
# s1.update(45)
print(s1)

s1.update('abc')
print(s1)

s1.update([45,56,78])
print(s1)

s1.update({'x':'abc', 'c':'78'})    # 只能添加其中的key
print(s1)

# 二：删
# 1.remove(x) x:表示需要被删除的元素，如果x不存在，则直接报错
s1 = {12,56,45,78,89}
s1.remove(12)
print(s1)
# s1.remove(100)      # KeyError: 100

# 2.pop(): 因为集合是无序的，表示随机删除一个
s1 = {12,56,45,78,89}
s1.pop()
print(s1)

print('*' * 52)
# 3.discard() x:表示需要被删除的元素，如果x不存在，不报错
s1 = {12,56,45,78,89}
s1.discard(12)
print(s1)
s1.discard(100)


# 4.clear()
s1.clear()
print(s1)       # set()

# 三：查
s1 = {12,56,45,78,89}
print(len(s1))
print(max(s1))
print(min(s1))

s2 = s1.copy()


# 四、转换
# int()/ float() /bool()/ str()/list()/tuple()/dict()/set()

# list()/tuple()/set() :可以进行相互转换