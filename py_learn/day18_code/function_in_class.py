#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 动态绑定属性
# 特征，行为
# 设计类
class Person():
    __slots__ = ('name','age')
    # 1.特征：属性，类属性，实例属性（动态绑定）
    # 类属性
    palce = '地球'
    def __init__(self, name, age):
        # 实例属性/ 对象属性
        self.name = name
        self.age = age

    # 2.行为：函数/方法
    # 类函数
    @classmethod
    def check(cls):     # cls:表示当前类，如果需要自定义参数，添加在cls的后面即可
        print('类函数~~~~check', cls)       # <class '__main__.Person'>
        # 函数之间的相互调用
        # a.在类函数中调用实例函数和静态函数
        obj = cls('张三', 11) # 创建对象，调用__init__，等价于 obj = Person('张三', 11)
        obj.show()

        cls.func1()
        obj.func1()

        cls.cheeck1()
        obj.cheeck1()

        # b.在类函数中访问类属性
        print(cls.palce)
        print(obj.palce)

    @classmethod
    def cheeck1(cls):
        print('类函数~~~~~~~~check111')

    # 实例函数/对象函数
    def show(self):     # self:当前对象，如果需要自定义参数，添加在self的后面即可
        print('实例函数~~~~show')
        # c.在实例函数中调用类函数或静态函数
        self.cheeck1()      # per.cheeck1()
        self.func1()
        Person.cheeck1()
        Person.func1()

        # d.在实例函数中调用实例函数
        self.show1()

    def show1(self):
        print('show~~~~1111')

    # 静态函数
    # 静态函数中一般不调用 实例函数或者类函数
    @staticmethod
    def func1():        # 只需要定义自定义的参数即可
        print('静态函数~~~~func')

# 通过  类名 或者 对象调用 类函数 和静态函数
Person.check()
Person.func1()
per = Person('小米', 21)
per.check()
per.func1()

# 只能通过 对象调用实例函数
per.show()


print(Person)       # <class '__main__.Person'>
# 注意1. ；cls 和self 都是系统自动完成传参的，无需手动传参
# 注意2. 类中函数相互调用，都必须要遵循
#       通过类名【cls】 或者对象【cls创建对象或者self】 调用


# 应用：定义工具类
# 工具类：目的是使用更加方便，所以在工具类中定义的函数  一般是类函数或者静态函数，
#       因为调用的时候，无需创建对象，可以通过类名直接调用

class Number():
    @staticmethod
    def add(num1,num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2

    @staticmethod
    def mul(num1, num2):
        return num1 * num2

    @staticmethod
    def div(num1, num2):
        return num1 / num2

print(Number.add(19, 23))
print(Number.sub(19, 23))
print(Number.mul(19, 23))
print(Number.div(19, 23))

class Newqw():
    pass

