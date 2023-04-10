#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import string
# input_str = input("请输入信息：")
# letters_count = 0
# num_count = 0
# other_count = 0
# for ch in input_str:
#     if ch in string.ascii_letters:
#         letters_count += 1
#     elif ch.isdigit():
#         num_count += 1
#     else:
#         other_count += 1
# print(f"字符串的长度是{letters_count},"
#       f"数字的长度{num_count},其他字符的长度是{other_count}")

# song_scripts = '这些年一个人，风也过，雨也走，有过泪，有过错' \
#                ', 还记得坚持甚么，真爱过才会懂，会寂寞会回首，' \
#                '终有梦终有你在心中。朋友一生一起走，那些日子不再有，一句话，一辈子，一生情，一杯酒。朋友不曾孤单过，一声朋友你会懂，还有伤，还有痛，还要走，还有我。'
# friends_str = '朋友'
# print(song_scripts.count(friends_str))

# ignore_words = ['性','色情','爆炸','恐怖','枪','军火']
# user_input = input("聊天内容：")
# for word in ignore_words:
#     if word in user_input:
#     #if user_input.find(word) != -1:
#         user_input = user_input.replace(word, "*" * len(word))
# print(user_input)
# # 军火走私所涉及的大使馆爆炸问题
# # **走私所涉及的大使馆**问题

# 4.输入一个用户名，判断用户名是否合法。用户名要求：由英文字母或数字组成，长度是6到12位
# import string
# user_name = input("用户名：")
# count = 0
# if 6 <= len(user_name) <= 12:
#     for ch in user_name:
#         if ch.isdigit() or ch in string.ascii_letters:
#             count += 1
# else:
#     print("不合法")
# if len(user_name) == count:
#     print('合法')
# else:
#     print('不合法')

# 5.随机生成长度为5的验证码， 验证码的组成是英文字母或者数字
# 生成 验证码
# 方式一
# import string
# import random
# random_str = ''
# for _ in range(5):
#     random_str += random.choice(string.ascii_letters + string.digits)
# print(random_str)

# 方式二
import string,random
random_str = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
print(random_str)

# 方式三
random_str = "".join(random.sample(string.ascii_letters + string.digits, 5))
print(random_str)

# str1 = "1,2,3"
# str_list = []
# for ch in str1:
#     if ch.isdigit():
#         str_list.append(ch)
# print(str_list)

# input_str = input("请输入内容：")
# if input_str[-3:] == '.py':
#     print(True)
# else:
#     print(False)

# import string
# input_str = input("请输入内容：")
# num_str = ''
# for ch in input_str:
#     # if ch in string.digits:
#     if ch.isdigit():
#         num_str += ch
# print(num_str)


# import string
# user_name = input("用户名：")
# if user_name[0] in string.ascii_uppercase:
#     for ch in user_name:
#         if ch.isdigit() or ch in string.ascii_letters:
#             pass
#         else:
#             print("不合法")
#             break
#     else:
#         print("合法")
# else:
#     print('不合法')

# 交集
# input_str0 = input("输入字符串0：")
# input_str1 = input("输入字符串1：")
# common_str = ''
# input_str0_set = set(input_str0)
# input_str1_set = set(input_str1)
# common_str_list = input_str0_set.intersection(input_str1_set)
# if len(common_str_list) == 0:
#     print("公共字符不存在")
# else:
#     for ch in common_str_list:
#         common_str += ch
#     print(common_str)

# 4.如下字符串:  "01#张三#60-02#李四#90-03#王五#70",
# 每一部分表示  学号#姓名#分数，提取学生信息存放于列表中，并按照成绩对学生降序排序
str1 = '01#张三#60-02#李四#90-03#王五#70'
information_list = []
str1_list = str1.split('-')
print(str1_list)    # ['01#张三#60', '02#李四#90', '03#王五#70']
for subli in str1_list:
    single_info_dict = {}
    subli = subli.split('#')    # ['01', '张三', '60'], ['02', '李四', '90'],['03', '王五', '70']
    # information_list.append(dict(zip(['学号','姓名','成绩'], subli)))   ********
    single_info_dict['学号'] = subli[0]
    single_info_dict['姓名'] = subli[1]
    single_info_dict['分数'] = subli[2]
    information_list.append(single_info_dict)
print(information_list)

# 排序
score = []
for info in information_list:
    score.append(info['分数'])
score.sort(reverse=True)
information_list = [info for sc in score for info in information_list if sc == info['分数']]
print(information_list)
