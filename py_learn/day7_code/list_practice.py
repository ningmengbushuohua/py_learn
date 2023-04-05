#!/usr/bin/env python3
# -*- coding: utf-8 -*-
names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']
# names.insert(-1, 'alex')
# print(names)
#
# names[3] = '珊珊'
# print(names)
#
#
# names.insert(2, ['oldboy', 'oldgirl'])
# print(names)
#
# print(names.index('peiqi'))
#
# list1 = [1,2,3,4,2,5,6,2]
# names.extend(list1)
# print(names)
#
# for i in range(4, 8):
#     print(names[i])
# for i in range(2, 11,2):
#     print(names[i])
# print('**' * 25)
# print(names)
# for i in range(-3,0,1):
#     print(names[i])
# print('**' * 25)
# print(names)

# for n,element in enumerate(names):
#     if n % 2 == 0:
#         element = -1
#     print(n, element)

# for n,element in enumerate(names):
#     if n % 2 == 0:
#         element = -1
#     print(n, element)

# names = ['鲁班七号','后裔', '狄仁杰', '黄忠', '孙尚香']
# print(names[names.index('黄忠')])
#
# print(names[-2])

nums = [1, 2, 3,1, 4, 2, 1 ,3, 7, 3, 3]
# for n,num in enumerate(nums):
#     if n % 2 == 1:
#         print(num)

# for i in range(1, len(nums), 2):
#     print(nums[i])

# scores = [90, 89, 67, 98, 75, 87, 54, 88]
# score1, score2 = eval(input("请输入两个成绩，用逗号隔开"))
# print(score1, type(score1))
# print(score2, type(score2))
# scores.append(score1)
# scores.insert(0, score2)
# print(scores)

# nums = [1, 2, 5, 9]
# for n,num in enumerate(nums):
#     num *= 2
#     nums[n] = num
# print(nums)

# 自定义一个数字列表，获取该列表中元素的最小值，注意: 自己实现，不能使用min函数
# 假设法
# nums = [10, 2, 5, 9, 56, 8, 98]
# min_value = nums[0]
# for num in nums:
#     if num < min_value:
#         min_value = num
# print(min_value)
#
# nums = [10, 2, 5, 9, 56, 8, 98]
# nums.sort()
# print(nums[0])

# list1 = ['mon','sun','sat','fri','thu','wed']
# list2 = ['sun','wed','thu']
#
# for li_2 in list2:
#     if li_2 in list1:
#         list1.remove(li_2)
# print(list1)

# spring = [3,4,5]
# summer = [6,7,8]
# fall = [9,10,11]
# winter = [12,1,2]
# month = int(input("请输入月份"))
# if month in spring:
#     print("春天")
# elif month in summer:
#     print("夏天")
# elif month in fall:
#     print("秋天")
# elif month in winter:
#     print("冬天")
# else:
#     print("无法识别")

# 要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
# while True:
#     num = eval(input("请输入员工的数量"))
#     slary = eval(input("请输入员工的薪资"))
#     if num == 0 or len(slary) != num:
#         print("输入错误")
#         continue
#     for slary_temp in slary:
#         if int(slary_temp) < 0:
#             print("输入错误")
#             continue
#     print(f"员工的数量是{num}")
#     print(f"薪资明细{slary}")
#     print(f"平均工资{sum(slary) / num}")
#     break
#方法二：
# emp_num = 0
# salary_sum = 0
# salary_list = []
# while True:
#     salary = input(f"请输入第{emp_num}位员工的薪资【按q或者Q退出】：")
#     if salary == 'q' or salary == "Q":
#         print("输入结束，退出")
#         break
#     if float(salary) < 0:
#         print("薪资小于0，输入错误，请重新输入")
#         continue
#     emp_num += 1
#     salary_sum += float(salary)
#     salary_list.append(float(salary))
# print(f"录入员工的数量：{emp_num},薪资明细：{salary_list}平均薪资：{round(salary_sum / emp_num)}")

weight = 0.00001
total = 0
for i in range(64):
    total += weight * (2 ** i)
print(total)

# 方式二：
num = 1
total = num
for _ in range(63):
    num = 2 * num
    total += num
print(f"重量{total * weight} kg")

money = 100000
count = 0
while money >= 5000:
    if money > 50000:
        money *= 0.95
        count += 1
    else:
        money -= 5000
        count += 1
print(count)