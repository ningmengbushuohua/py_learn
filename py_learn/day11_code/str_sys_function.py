#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字符串属于不可变的数据类型，所以但凡设计的字符串更改的操作，都是生成了一个新的字符串

# 1.写代码，有如下变量，请按照要求实现每个功能
# name = "gouguoQ "


# a.移除name变量对应值的两边的空格，并输出移除后的内容
'''
strip():去除一个指定字符串中两端指定的子字符     ***********
lstrip():去除一个指定字符串中左边指定的子字符
rstrip():去除一个指定字符串中右边指定的子字符
'''
import stringprep

name = "   gouguoQ "
# 1. 如果未指定子字符，则默认去除的是空格
a1 = name.strip()
print(name)     #    gouguoQ
print(a1)

a2 = name.lstrip()
print(a2)
a3 =name.rstrip()
print(a3)

# 2. 也可以指定需要去除的字符
name = '*******shsu***'
a1 = name.strip('*')
print(a1)
a2 = name.lstrip('*')
print(a2)
a3 =name.rstrip('*')
print(a3)
print('*' * 20)

# b.判断name变量对应的值是否以"go"开头，并输出结果
'''
startswith()；判断一个字符串是否是以指定自字符串开头【前缀】  *****
'''
name = "gouguoQ "
b1 = name.startswith('go')
print(b1)
# c.判断name变量对应的值是否以"Q"结尾，并输出结果
'''
endswith():判断一个字符串是否是以指定自字符串结尾【后缀】  *****
'''
c1 =name.endswith('Q')
print(c1)

print('*' * 20)
# d.将name变量对应的值中的"o"，替换为"p"，并输出结果
'''
replace(old,new):将原字符串中的old替换为new			
映射替换：
	maketrans():生成映射表
	translate():根据映射表将指定字符串中的指定字符替换为映射表中对应的字符
'''
name = "gouguoQooo "
# 1.默认情况下，全部替换
d1 = name.replace('o', 'p')
print(d1)
# 2.可以控制替换的次数
d1 = name.replace('o', 'p', 3)
print(d1)
# 3.映射替换:   用于简单的加密，可以自定义加密规则
name = '12569826023546'
# 第一步：生成映射表【制定规则】，
# 注意1：下面代码中的str是系统模块，不是变量名
# 注意2：在生成映射表示，两个字符串的长度必须相等
# ValueError: the first two maketrans arguments must have equal length
table = str.maketrans('123456789','abcdefghi')
# 第二步：通过映射表翻译指定字符串
d3 = name.translate(table)
print(d3)

# 练习
name = "gouguoQooo "
table = str.maketrans('o','p')
d4 = name.translate(table)
print(d4)

# e.将name变量对应的值根据"o"分割，并输出结果
'''
# split():使用指定的子字符串将原字符串进行分割，得到一个列表  【字符串-----》列表
注意：字符串中的split只能进行分割有规律的字符串
    如果需要分割没有规律的字符串，则使用正则表达式中的split()    ********
'''
# 1. 默认全分割
name = "gouguoQc "
list1 = name.split('o') # ['g', 'ugu', 'Qc ']
print(list1)

# 2.可以自定义分割次数
name = "gouguoQcoooooop "
list1 = name.split('o', 3)
print(list1)    # ['g', 'ugu', 'Qc', 'ooooop ']

# 3.如果分割符出现在字符串的最后一位，则最终列表的最后一个元素是''
name = "gouguoQcooooooo"
list1 = name.split('o')
print(list1)    # ['g', 'ugu', 'Qc', '', '', '', '', '', '', '']

# n.利用下划线将列表li = ['gou', 'guo', 'qi']的每一个元素拼接成字符串gou_guo_qi
'''
join()：使用指定的子字符串将列表中的元素连接【列表-----》字符串】	******
'''
li = ['gou', 'guo', 'qi']
# 语法：连接字符串.join(列表)，注意此时该列表中的元素一定是字符串
n = "_".join(li)
print(n)
n = "".join(li)
print(n)

# g.将name变量对应的值变大写，并输出结果
# h.将name变量对应的值变成小写，并输出结果
'''
**********
upper():小——》大
lower():大---》小
swapcase():大---》小  小----》大
capitalize():首单词的首字母大写，其他全部小写，英文句子
title():每个单词的首字母大写，其他全部小写
'''
name = 'this is a TEXT'
print(name.upper())
print(name.lower())
print(name.swapcase())
# 【面试题】
print(name.title()) # This Is A Text
print(name.capitalize())    # This is a text

name = "gouguoQcQ"
# i.请输出name变量对应的值的第二个字符
print(name[1])  # 访问字符串中的字符
# j.请输出name变量对应的值的前三个字符
print(name[:3])
# k.请输出name变量对应值的后2个字符
print(name[-2:])
print(name[len(name) - 2:])

# m.获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
print(name[:-1])
# l.请输出name变量中的值"Q的索引的位置
'''
find():从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，
        如果查找不到返回-1				********
rfind():从右往左进行检索
index()：从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，
        如果查找不到则直接报错		
rindex():从右往左进行检索
'''
name = "gQugQoQcQ"
# 1. index 和find 都是从左往右查找指定字符在原字符串中第一次出现的索引，默认全局查找
l1 = name.index('Q')
print(l1)
l1 = name.find('Q')
print(l1)

# 2.给定一个索引的区间，可以局部查找，仍然遵循前闭后开区间
# 3.如果子字符串，index会直接报错， find返回-1
l1 = name.index('Q',1,3)
print(l1)
l1 = name.find('Q',1,3)
print(l1)

# l1 = name.index('Q',2,4)      # ValueError: substring not found
# print(l1)
l1 = name.find('Q',2,4)
print(l1)   # -1
