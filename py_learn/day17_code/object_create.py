#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 创建对象/实例化对象/类的实例化
# 对象也被称为实例


# 1.未定义构造函数 __init__
# 语法： 变量 = 类名()
class Person():
    pass

p1 = Person()
print(p1)       # <__main__.Person object at 0x000001CBA332CBE0>
print(id(p1))
p2 = Person()
print(p2)       # <__main__.Person object at 0x000001CBA332CBB0>
print(id(p2))

print('*' * 92)
# 2.定义构造函数 __init__： 推荐
# 语法： 变量 = 类名(xx,xx,xx...)  xx,xx,xx... 类似于函数中的传参【实参】

class Animal():
    # 构造函数之一：__init__,表示初始化。给对象初始化
    # 注意：形如__xx__命名的函数，在Python 中被称为魔术函数【魔术方法】，此类函数无需手动调用，都会在特定的场景下自动调用
    # __init__: 当创建对象时，会自动调用__init__函数
    # self:无需传参， 当创建对象时，会将当前创建的对象自动传参给self, self:当前对象
    def __init__(self,name,age,kind):
        # print('init----',id(self),name,age,type)
        # 语法：对象.变量 = 值， 表示给当前对象进行特征的描述
        self.name = name       # 等号前 ，当前对象的特征，等号后，来源于函数的参数
        self.age = age
        self.kind = kind
# 注意：创建对象的时候，需不需要传参，传几个参数，一定要和__init__函数匹配
a1 = Animal('小白',3,'猫')
print('a1:', id(a1))    # a1 和self,表示的是同一个对象，同一个对象的地址
print(a1.name, a1.age, a1.kind)

a2 = Animal('狗子', 4, '田园犬')
print('a2:', id(a2))
print(a2.name, a2.age, a2.kind)


# 如果不使用__init__，弊端
class Animal():
    pass

a1 = Animal()
a1.name = '小白'
a1.age = 3
a1.kind = '猫'
print(a1.name, a1.age, a1.kind)

a2 = Animal()
a2.name = '旺财'
a2.age = 4
a2.kind = '土狗'
print(a2.name, a2.age, a2.kind)