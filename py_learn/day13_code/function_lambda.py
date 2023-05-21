#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 语法：lambda  形参列表:返回值
# 1. 和def定义的函数进行对比
def func(n):
    print('111')
    return n + 5
print(func)     # 函数本身 <function func at 0x0000014055F9F280>
# r1 = func(15) # 调用函数
# print(r1)

# 注意1: 在匿名函数中，返回值前面无需要书写return
# 注意2：在匿名函数中，一般除了参数和返回值外，无法添加其他代码
func2 = lambda n: n + 5
print(func2)        #函数本身  <function <lambda> at 0x000001D8D503C790>
r2= func2(45)    # 调用函数
print(r2)

# 2.匿名函数的参数部分，仍然可以使用默认参数，不定长参数，调用可以使用关键字参数
fun3 = lambda x,y:x ** 2 + y ** 2       # 必须参数
print(fun3(3,4))
fun3 = lambda x=0,y=0:x ** 2 + y ** 2   # 默认参数
print(fun3())
print(fun3(3,4))

fun3 = lambda *y:y
print(fun3(3,4,56,6,2,7))

# 3.应用：匿名函数常用于给其他函数传参
# 列表.sort()
# a. 如果列表中的元素支持大小比较，则会进行排序
list1 = [2,55,6,9]
list1.sort()    # 升序
print(list1)

list1 = [2,55,6,9]
list1.sort(reverse=True)    # 降序
print(list1)

# b. 按照学生的成绩降序排序
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
# 错误写法
# students.sort(reverse=True)     # TypeError: '<' not supported between instances of 'dict' and 'dict'

#正确写法
'''
列表.sort(key,reverse)
    key: 用来指定列表中元素排序的规则  或者用于列表中元素不支持大小比较的情况
        key的值必须是一个函数,只需要书写函数名
工作原理：将函数中的元素依次取出，然后传参给对应的func，func的返回值就是排序的规则，
        所以要求该返回值必须能比较大小
'''

# 1>
# 默认的排序规则 :ascii 码表
namelist = ['ss','x','ssoo']
namelist.sort()
print(namelist)

# 自定义规则：根据长度
namelist = ['ss','x','ssoo']
namelist.sort(key=len)
print(namelist)
'''
'ss','x','ssoo'
 2, 1 , 4
 1,2,4
 'x','ss','ssoo'
'''

# 2>
# def rule(stu_dict):
#     return stu_dict.get('score')
# students.sort(key=rule,reverse=True)
# print(students)

students.sort(key=lambda stu_dict:stu_dict['age'], reverse=True)
print(students)

# 匿名函数的使用场景，给另一个函数传参