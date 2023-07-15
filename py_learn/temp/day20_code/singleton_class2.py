# 单例类实现2
# 【面试题】单例类
# 需求： 书写一个装饰器，可以使得任意一个类都成为装饰器
def wrapper(cls):
    # key；被装饰的对象cls   value:类可以创建的唯一对象
    instance_dict = {}
    def inner(*args,**kwargs):
        if not instance_dict:
            instance_dict[cls] =  cls(*args,**kwargs)
        return instance_dict[cls]
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