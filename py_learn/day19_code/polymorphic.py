# 一种事物的多种体现形式，举例：动物有很多种
class Animal():
    pass
class Cat(Animal):
    pass
class SmallCat(Cat):
    pass

# isinstance(对象，类型)  ：判断 对象是否是制定的类型
sc = SmallCat()     # 多态的体现
print(isinstance(sc, SmallCat))
print(isinstance(sc, Cat))
print(isinstance(sc, Animal))
print(isinstance(sc, object))

# 定义时并不确定是什么类型，要调用的是哪个方法，只有运行的时候才能确定调用的是哪个
class Animal():
    def style(self):
        print('walking')
class Cat(Animal):
    pass
class Dog(Animal):
    pass

class Fish(Animal):
    def style(self):
        print('Swinmming')

class Brid(Animal):
    def style(self):
        print('flying')

def show(ani):  # ani 就是多态的体现
    print(type(ani))
    ani.style()

d = Dog()
c = Cat()
f = Fish()
b = Brid()

show(d)
show(c)
show(f)
show(b)