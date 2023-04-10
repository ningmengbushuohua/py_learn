#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 3.统计用户输入的内容中有几个数字，几个字母？
'''
不建议使用：
isalpha():一个字符串非空并字符全部是字母才返回True
isalnum():一个字符串非空并字符是字母或者数字才返回True

原因：判断的依据是ASCII表，ASCII码表 不包含中文，使用isalpha()和isalnum(),
    则中文会被识别为字母
'''

# data = input("请输入内容：")
# 不严谨的写法：
# letters_count = 0
# digits_count = 0
# for ch in data:
#     if ch.isalpha():
#         letters_count += 1
#     if ch.isdigit():
#         digits_count += 1
# print(f"字母{letters_count},数字{digits_count}")

# 建议的写法
# 方式一：
# letters_count = 0
# digits_count = 0
# for ch in data:
#     if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
#         letters_count += 1
#     if ch.isdigit():
#         digits_count += 1
# print(f"字母{letters_count},数字{digits_count}")


# 方式二：
import string
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.digits)
# letters_count = 0
# digits_count = 0
# for ch in data:
#     if ch in string.ascii_letters:
#         letters_count += 1
#     if ch.isdigit():
#         digits_count += 1
# print(f"字母{letters_count},数字{digits_count}")


# 4.编写敏感词语过滤程序，提示用户输入内容，
# 如果用户输入的内容中包含特殊的字符，如山寨 水货，则将内容替换为*****
data = input("请输入内容：")
words = ['水货','山寨','高仿','人民币','最','第一']

for wo in words:
    if data.find(wo) != -1: #判断是否存在  wo in  data
        data = data.replace(wo, "*" * len(wo))
print(data)