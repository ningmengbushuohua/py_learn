#!/usr/bin/env python3
# -*- coding: utf-8 -*-


num1_list = [[0 for i in range(3)] for j in range(10)]
print(num1_list)
temp = 0
# for i in range(1,10):
#     for j in range(i + 1,10):
#         for k in range(j + 1, 10):
#             if i + j  == k:
#                 num1_list[temp][0] = i
#                 num1_list[temp][1] = j
#                 num1_list[temp][2] = k
#                 temp += 1
# print(num1_list)
# print(temp)

# [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [1, 8, 9]
# [2, 3, 5], [2, 4, 6], [2, 5, 7], [2, 6, 8], [2, 7, 9]
# [3, 4, 7], [3, 5, 8], [3, 6, 9]
# [4, 5, 9]


# 1 5 9    2  6  7    3  4  8
#
# 4 5 9    2 6 8    none

# 3 4 7   2 6 8
# 3 5 8    2 4 6   2 7 9       1 6 7

#3 6 9    2 5 7
