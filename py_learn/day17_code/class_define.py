#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
(大驼峰命名)，缩进
# 类体一般包含两部分内容：对类的特征描述和行为描述

'''

# 1.定义一个空类,
class Student():
    pass
class StudentInfo():
    pass

# 2.非空类
def check():
    print('check******start')
    print('check******end')

class MyClass():
    print('33333~~~~~start')
    # 类体
    # 1.类的特征描述，变量
    num = 10
    name = 'zhangsan'
    # 2.类的行为描述，函数
    def show(self):
        print('showing')
    def func1(self):
        print('22asfw')

    print('33333~~~~~end')

'''
总结：
    a.类的定义和函数的定义类似，但是，一个函数定义完毕之后，只有调用才会执行其中的代码
      类定义完毕之后，其中的代码立马会被加载
    b.同一个py文件中可以定义多个类，但是在实际项目开发中，由于每个类实现的代码可能较为复杂，类的定义建议一个py文件一个类【创建一个包，一个模块中定义一个类】
    c.当一个类定义完成，类中的内容被称为类体，又被称为类的成员，当类被加载的时候，类中的成员也会被加载
'''
# 注意：和函数的使用相同，类也会引入新的作用域，所以在类中定义的变量、函数，在类的外面无法直接访问
