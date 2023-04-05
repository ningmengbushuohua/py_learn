#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 注意：因为列表是可变的， 所以 涉及到增加、删除、修改的操作，都是在列表内部直接操作的

# 一：增
# 1. list.append(obj)  在列表末尾添加新的对象  ***** 特点： 可以追加任意类型的元素
list1 = [1,2,3]
print(list1)
# 正确写法
list1.append('lol')
print(list1)
# 错误写法
r = list1.append(False)
print(r)        # None

#
#seq ：序列
# 2. list.extend(seq) 在列表末尾一次性追加另一个序列【列表、元组、字符串】中的多个值（用新列表扩展原来的列表）
list1 = [1,3,6]
list2 = [1,5,6]
list1.extend(list2)
print(list1)

list1.extend('list2')
print(list1)

# 3.list.insert(index,obj)  将对象插入列表， 特点： 可以追加任意类型的元素
list1 = [1,3,6]
list1.insert(0, 'abc')
print(list1)       # ['abc', 1, 3, 6]

list1.insert(2, 'hello')
print(list1)        # ['abc', 1, 'hello', 3, 6]
#

# 二： 删
# 1.list.remove(obj)   移除列表中某个值的第一个匹配项   ****************
# 直接删除
list2 = [256,6,36,89,56,89,89]
print(list2)
list2.remove(89)
print(list2)
list2.remove(89)
print(list2)
list2.remove(89)
print(list2)

# 2.list.pop(index)  移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 通过属于索引删除
list2 = [256,6,36,89,56,89,89,56,8]
print(list2)
# a. 默认删除最后一个元素
# list2.pop()
# print(list2)

# b.删除指定的元素
list2.pop(2)    # 索引 2 的元素
print(list2)

# c. 注意： pop 的本意不是删除， 是弹出，
# 所以 pop使用完毕后，如果在之后的代码中 使用被弹出的元素，则可以 用变量直接接出来

r = list2.remove(256)
print(r)  # None

r1 = list2.pop(-2)
print(r1)   # 56


# 3. list.clear() 清空列表
list2.clear()
print(list2)

#  4. del  xxx
list2 = [256,6,36,89,56,89,89,56,8]
del list2[0]    # 删除列表中的某个位置的元素
del list2       # 删除列表

# 三： 改
# list.reverse() ：  反转列表中元素
list3 = [256,6,36,89,56,89,89,56,8]
list3.reverse()     # 注意此处也不能用变量接出来
print(list3)


# list.sort(key=None,reverse=False) ： 对原列表进行排序
# a. 升序
list3 = [256,6,36,89,56,89,89,56,8]
list3.sort()
print(list3)

# b. 降序
list3 = [256,6,36,89,56,89,89,56,8]
list3.sort(reverse=True)
print(list3)


# 四。查
list4 = [256,6,36,89,56,89,89,56,8]
# 1. len(list)  获取列表元素个数
print(len(list4))

# 2.max(list)  返回列表元素最大值
print(max(list4))

# 3.min(list) 返回列表元素最小值
print(min(list4))

# 4. list.count(obj) 统计某个元素在列表中出现的次数
n = list4.count(8)
print(n)

# 优化
list4 = [256,6,36,89,56,89,89,89]
print(list4)
count = list4.count(89)
for n in range(count):
    list4.remove(89)
print(list4)

print('***' * 52)

# 5. list.index(seq, start ,end)  从列表中找出某个值第一个匹配项的索引位置
list4 = [256,6,36,89,56,89,89,89]
# a. 全局查找
print(list4.index(89))  # 3
# b. 指定区间内的查找, 仍然遵循 ，包头不包尾
# print(list4.index(89,2,4))  # 3
# print(list4.index(89,1,3))  # ValueError: 89 is not in list
