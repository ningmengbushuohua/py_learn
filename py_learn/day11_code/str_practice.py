#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
a = "aAsmr3idd4bgs7Dlsf9eAF"
# a.请将a字符串的大写改为小写，小写改为大写
a1 = a.swapcase()
print(a1)
# b.请将a字符串的数字取出，并输出成一个新的字符串
# 方式一：
new_a = ''
for ch in a:
    if ch in [str(i) for i in range(10)]:
        new_a += ch
print(new_a)

# 方式二：
new_a = ''
for ch in a:
    if ch.isdigit():
        new_a += ch
print(new_a)

# 方式三：
# import  re
# r = "".join(re.split(r'[^0-9]', a))
# print(r)


# c.请统计a字符串每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
c = a.lower()
count_dict = {}
for ch in c:
    count_dict[ch] = c.count(ch)
print(count_dict)

# d.输出a字符串出现频率最高的字母
c = a.lower()
count_dict = {}
for ch in c:
    count_dict[ch] = c.count(ch)

max_count = max(count_dict.values())
max_list = []
for ch,count in count_dict.items():
    if count == max_count:
        max_list.append(ch)
print(f"出现频率最高的字符是：{max_list},出现的次数是{max_count}")

# e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False
substr = 'boy'
a = "aAsmr3idd4bygs7Dlsof9eAF"
# 方式一：统计个数
count = 0
for ch in substr:
    if ch in a:
        count += 1
if count == len(substr):
    print(True)
else:
    print(False)

# 方式二：使用集合的去重性
s1 = set(a)
s1.update(substr)
print(s1)
if len(set(a)) == len(s1):
    print(True)
else:
    print(False)

# 方式三：交集
s1 = set(a)
s2 = set(substr)
s3 = s1.intersection(s2)
print(s3)
if len(s3) == len(s2):
    print(True)
else:
    print(False)
