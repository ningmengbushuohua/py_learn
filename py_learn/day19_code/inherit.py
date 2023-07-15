# 继承的使用
# 单继承 多继承

# 1. 单继承
# 父类
class Person():
    def __init__(self,name,age):
        print('父类的---init')
        self.name = name
        self.age = age
    def eat(self):
        print('eating-------')

# 子类
# a.子类中没有定义__init__. 创建子类对象。调用父类的__init__
class Doctor(Person):
    pass

d1 = Doctor('王大夫',43)
print(d1.age, d1.name)
d1.eat()


# b.如果子类中自己定义了__init__，且定义了 特有的的属性，则在子类中的__init__中调用父类的__init__
class Student(Person):
    def __init__(self,name,age,score):
        # 在子类中的__init__中调用父类的__init__
        # 方式一：super(当前类，self).__init__(参数列表)
        # super(Student,self).__init__(name,age)

        # 方式二：super().__init__(参数列表)
        # super().__init__(name,age)

        # 方式三： 父类.__init__(self,参数列表)
        Person.__init__(self, name, age)

        self.score = score
    def study(self):
        print('studying-------')
stu = Student('黎明',21,88)
print(stu.score)
print(stu.name, stu.age)
stu.eat()
stu.study()


# 多继承
class Flyable():
    def fly(self):
        print('flying-----')
class Runable():
    def run(self):
        print('running-----')

class Brid(Flyable,Runable):
    pass

bird = Brid()
bird.run()
bird.fly()

# 继承的好处，简化代码，复用性，可读性