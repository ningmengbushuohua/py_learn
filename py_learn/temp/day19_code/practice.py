# class Number():
#     __slots__ = ('num1', 'num2')
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def addition(self):
#         return self.num1 + self.num2
#
#     def subration(self):
#         return self.num1 - self.num2
#
#     def multiplication(self):
#         return self.num1 * self.num2
#
#     def division(self):
#         return self.num1 / self.num2
#
# num = Number(23,12)
# print(num.addition())
# print(num.subration())
# print(num.multiplication())
# print(num.division())

# 此处为错误写法
# 分别定义Circle（圆）类和点（Point）类，计算该圆的周长和面积，并判断某点与该圆的关系
# class Circle():
#     __slots__ = ('hengzuobiao','zongzuobiao','banjing')
#     def __init__(self,h,z,r):
#         self.hengzuobiao = h
#         self.zongzuobiao = z
#         self.banjing = r
#     def area(self):
#         return self.banjing ** 2 * 3.14
#     def perimeter(self):
#         return 2 * 3.14 * self.banjing
#
# class Point(Circle):
#     __slots__ = ('p_hengzuobiao','p_zongzuobiao')
#     def __init__(self,h,z,ph,pz,r):
#         super().__init__(h,z,r)
#         self.p_hengzuobiao = ph
#         self.p_zongzuobiao = pz
#
#     def distance(self):
#         distance = ((self.hengzuobiao - self.p_hengzuobiao) ** 2
#         + (self.zongzuobiao - self.p_zongzuobiao) ** 2) ** 0.5
#         if distance > self.banjing:
#             return False
#         return True
#
# c1 = Circle(1,2,3)
# print(c1.area())
# print(c1.perimeter())
# # 关系
# p1 = Point(1,2,3,7,3)
# print(p1.distance())


# class Account():
#     __slots__ = ('name', '__money')
#     def __init__(self,name):
#         self.name = name
#         self.__money = 0
#
#     def insert(self, money):
#         self.__money += money
#
#     def desert(self,money):
#         if money > self.__money:
#             print('余额不足')
#             return False
#         self.__money -= money
#     def show(self):
#         print(f'当前的余额为{self.__money}')
# a1 = Account('张三')
# a1.show()
# a1.insert(122)
# a1.show()
# a1.desert(23)
# a1.show()

# sutdents_list = []
# class Student():
#     __slots__ = ('mid','name','age','sex','score')
#     def __init__(self,mid,age,name,sex,score):
#         self.mid = mid
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.score = score
#
# class Grade():
#     def show_all(self):
#         print(sutdents_list)
#     def show_by_mid(self,mid):
#         for info in sutdents_list:
#             if info.mid == mid:
#                 print(info)
#         else:
#             print('暂无当前学生')
#     def show_degrade(self):
#         temp_list = []
#         for info in sutdents_list:
#             if info.score < 60:
#                 temp_list.append(info)
#         print(temp_list)
#
#     def show_by_jiangxu(self):
#         sutdents_list.sort(key=lambda x:x.score, reverse=True)


# 分别定义Circle（圆）类和点（Point）类，计算该圆的周长和面积，并判断某点与该圆的关系
# import math
# class Circle():
#     # center_point： 点的对象
#     __slots__ = ('center_point','radius')
#     def __init__(self,center_point,radius):
#         self.radius = radius
#         self.center_point = center_point
#     def area(self):
#         return round(math.pi * self.radius ** 2,3)
#
#     def length(self):
#         return round(math.pi * self.radius * 2,3)
#
#     def judge(self,point):
#         # self:圆的对象，point:某点的对象
#         distance = math.sqrt((self.center_point.x - point.x) ** 2
#                              + (self.center_point.y - point.y) ** 2)
#         if distance > self.radius:
#             return '圆外'
#         elif distance == self.radius:
#             return '圆上'
#         else:
#             return '圆内'
#
#
# class Point():
#     __slots__ = ('x','y')
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# if __name__ == '__main__':
#     # 创建一个圆心的对象
#     center_point = Point(31,21)
#     # 创建一个圆的对象
#     c1 = Circle(center_point,10)
#     print(c1.area())
#     print(c1.length())
#
#     point1 = Point(45,34)
#     print(c1.judge(point1))

