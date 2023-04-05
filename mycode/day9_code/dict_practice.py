#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
# for key in dic.keys():
#     print(key)

# for key in dic:
#     print(key)

print("*"*50)
# for key in dic.keys():
#     print(dic[key])

# for key in dic:
#     print(dic[key])

# for key in dic.keys():
#     print(key, dic[key])

# for key in dic:
#     print(key, dic[key])
#
# for key, value in dic.items():
#     print(key,value)

dic['k4'] = 'v4'
print(dic)

dic.pop('k1')
print(dic)

if dic.get('k5'):   # 表示假的数据 0  0.0  ‘’  []  {}  ()  NOne  False
    dic.pop('k5')
else:
    print(dic.get('k5'))
    print(dic)

list1 = [11,22,11,33,44,55,66,55,66]
dict1 = {}
for li in list1:
    if dict1.get(li):
        dict1[li] += 1
    else:
        dict1[li] = 1
print(dict1)


students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
'15300022839'}
]

# count = 0
# for stu in students:
#     if stu.get('score') < 60:
#         count += 1
# print(count)

# dict1 = {}
# for stu in students:
#     if stu.get('score') < 60:
#         dict1[stu['name']] = stu['score']
# print(dict1)

# count = 0
# for stu in students:
#     if stu.get('age') < 18:
#         count += 1
# print(count)

# list1 = []
# for stu in students:
#     if stu.get('tel')[-1] == '8':
#         list1.append(stu.get('name'))
# print(list1)

# 最高分
# max_score_name = []
# max_score = students[0]['score']
# for stu in students:
#     if stu.get('score') > max_score:
#         max_score_name = []
#         max_score_name.append(stu.get('name'))
#         max_score = stu['score']
#     elif stu.get('score') ==  max_score:
#         max_score_name.append(stu.get('name'))
# print(max_score_name, max_score)

# students_list = []
# for stu in students:
#     if stu.get('gender') in ["男", "女"]:
#         students_list.append(stu)
# print(students_list)
# students = students_list

# list1 = [90,40,90,90,59,90]
# for i in range(0,len(list1)):
#     for j in range(0, len(list1) - 1):
#         if list1[j] > list1[j + 1]:
#             temp = list1[j+1]
#             list1[j+1] = list1[j]
#             list1[j] = temp
# print(list1)

# for i in range(len(students)):
#     for j in range(len(students) - 1):
#         if students[j]['score'] < students[j + 1]['score']:
#             students[j], students[j+1] = students[j+1], students[j]
# print(students)
#
#
# list1 = [i for i in range(3,100,10)]
# print(list1)
#
# list1 = [True, 17, "hello", "bye", 98, 34, 21]
# list2 = [li for li in list1 if type(li) == int]
# print(list2)

# list1 = ["good", "nice", "see you", "bye"]
# list2 = [len(i) for i in list1]
# print(list2)
#
# list2 = [f"{i}-{i+1}" for i in range(5)]
# print(list2)

# status_dict = {'张三': '已完成'}
# print("欢迎进入小程序")
# choice = input("1:查询，2:录入，请选择功能：")
# if choice == '1':
#     print('****----查询----****')
#     while True:
#         name =''
#         name = input("请输入学生姓名【按Q或者q退出】：")
#         if name in ['Q','q']:
#             print('程序结束，退出')
#             break
#         if status_dict.get(name):
#             print(name, status_dict[name])
#         else:
#             print('暂无此学生作业完成情况')
# else:
#     print('****----录入----****')
#     while True:
#         name,status ='',''
#         count = 0
#         name = input("请输入学生姓名【按Q或者q退出】：")
#         status = input("请输入学生作业完成情况【1：完成，0：未完成】【按Q或者q退出】：")
#         if name in ['Q','q'] or status in ['Q','q']:
#             print('录入结束，退出')
#             break
#         if status == '1':
#             status_dict[name] = '已完成'
#         elif status == '0':
#             status_dict[name] = '未完成'
#         else:
#             if count > 3:
#                 print('失败次数过多，禁止录入')
#                 break
#             count += 1
#             print('输入的作业完成情况有误，重新录入')
#
# print(f"学生的作业完成情况是{status_dict}")

# dict_list = [{"科目":"政治", "成绩":98}, {"科目":"语文", "成绩":77}, {"科目":"数学", "成绩":99}, {"科目":"历史", "成绩":65}]
# dict_list1 = [li for li in dict_list if li["成绩"] >= 70]
# print(dict_list1)

students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
'15300022839'}
]

students_list1 = [stu for stu in students if stu['gender'] in ['男', '女']]
print(students_list1)


