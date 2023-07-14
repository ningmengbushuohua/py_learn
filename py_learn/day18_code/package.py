#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 封装，
# 封装的本质：将类中的属性进行私有化
# 1.私有属性
# a.公开属性
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('张三',10)
# 通过对象可以直接访问
print(p1.name, p1.age)

print('*' * 89)
# a.私有属性/属性的私有化
class Person2():
    # 注意2:哪怕是私有属性，进行限制动态绑定时，也要书写__xxx形式
    __slots__ = ('__name', '__age')
    def __init__(self,name,age):
        #  注意：只需要在属性名的前面，添加两个下划线
        self.__name = name
        self.__age = age
    # 注意3：在当前类中，可以通过self.__xxx访问
    def show(self):
        print(f'姓名{self.__name},年龄{self.__age}')
p2 = Person2('张三',10)
# 通过对象无法直接访问
# print(p2.__name, p2.__age)      # AttributeError: 'Person2' object has no attribute '__name'
# print(p2.name, p2.age)  # AttributeError: 'Person2' object has no attribute 'name'
p2.show()

# 2. 私有函数
class Person3():
    __num = 55  # 类属性 也可以私有化
    def func(self):
        print('func~~~')
        # 调用私有函数，__func1()是实例函数
        self.__func1()
    def __func1(self):
        print('func1~~~1111')

p3 = Person3()
p3.func()
# p3.__func1()    # AttributeError: 'Person3' object has no attribute '__func1'

'''
【面试题】解释下面不同形式的变量出现在类中的意义
a:普通属性，也被称为公开属性，在类的外面可以直接访问             ****
_a:在类的外面可以直接访问,但是不建议使用，容易和私有属性混淆
__a:私有属性，只能在类的内部被直接访问。类的外面可以通过暴露给外界的函数访问    *****
__a__:在类的外面可以直接访问,但是不建议使用，因为系统属性和魔术方法都是这种形式的命名，
    如：__slots__  __init__  __new__  __del__，__name__,__add__,__sub__,__mul__等
'''