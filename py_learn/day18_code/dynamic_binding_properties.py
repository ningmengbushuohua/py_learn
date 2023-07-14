#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.类和对象的总结
# a.类的定义
class Person():
    # 类属性
    num = 88
    # b.构造函数__init__,在其中定义实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
# c. 创建对象
p1 = Person('小明', 18)
print(p1.name, p1.age)

# 2.
# a. 给对象动态绑定属性， 语法：对象.属性 = 值
# 默认情况下，可以给一个对象绑定任意名称、任意数量的属性
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person('小明', 18)
p1.hobby = '跳舞'
p1.score = 100
print(p1.name, p1.age, p1.hobby, p1.score)
p1.sss = 22
p1.xyz = 32

# b. 限制对象属性的动态绑定
# 如果需要限制对象属性的动态绑定，在类中定义__slots__ = ('属性名','属性名'....)
class Person():
    # 注意：如果限制当前类创建的对象只能绑定一个属性，注意元组的写法
    # __slots__ = ('name',)
    __slots__ = ('name', 'age', 'hobby', 'score')
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person('小明', 18)
p1.hobby = '跳舞'

print(p1.name, p1.age, p1.hobby, p1.score)
# p1.sss = 22  AttributeError: 'Person' object has no attribute 'sss'
# p1.xyz = 32