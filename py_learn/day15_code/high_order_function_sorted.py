#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
【面试题】列表中的sort函数和高阶函数sorted的区别和联系

1.调用语法：

	列表.sort(reverse,key=func),
      	sorted(iterable,reverse,key=func)
2.结果：sort是在原列表内部排序的，sorted是生成了一个新的列表
'''
list1=[2,23,442,41,2,4565,25,76]
list1.sort()
print(list1)

list1=[2,23,442,41,2,4565,25,76]
list2 = sorted(list1)
print(list2)

# 3.二者默认情况下都是升序排序,如果要降序，则都是设置reverse=True
list1=[2,23,442,41,2,4565,25,76]
list1.sort(reverse=True)
print(list1)

list1=[2,23,442,41,2,4565,25,76]
list2 = sorted(list1, reverse=True)
print(list2)

# 4.二者如果需要自定义排序规则，都是设置key=func
students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 100, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 98, 'gender': '男', 'tel':
'15300022839'}
]

# students.sort(key=lambda x:x['score'], reverse=True)
# print(students)

new_stu = sorted(students, key=lambda x:x['score'], reverse=True)
print(new_stu)