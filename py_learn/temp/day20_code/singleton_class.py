# 单例类 实例
# 1. 普通类
class Book():
    def __init__(self,name,date):
        self.name = name
        self.date = date
b1 = Book('坏蛋是怎么练成的',2001)
b2 = Book('爱情的本质',2002)

# 注意：如果两个变量中存储的数据的地址相同，则说明这两个变量中存储的是同一个对象
# 比较两个变量中是否存储的是同一个对象
print(b1 is b2)             # False
print(id(b1) == id(b2))     # False

# 2.单例类
# 【面试题】 单例类
# 需求： 书写一个装饰器，可以使得任意一个类都成为装饰器
def wrapper(cls):
    # 存储被装饰的类可以创建的惟一的对象
    instance = None
    def inner(*args,**kwargs):
        # cls(*args,**kwargs): 每执行一次，就会创建一个新的对象，要实现单例类，则只要控制该句代码只执行一次
        nonlocal instance
        if not instance:
            # print('if-----')
            instance =  cls(*args,**kwargs)
        return instance
    return inner
@wrapper
class Person():
    def __init__(self,name,age):
        print('init----')
        self.name = name
        self.age = age

p1 = Person('黎明',12)    # 创建对象
p2 = Person('张三',14)    # 获取对象
print(p1 == p2)         # True
print(id(p1) == id(p2))     # Ture

print(p1.name, p2.name)
p1.name = 'jack'
print(p1.name, p2.name) # jack