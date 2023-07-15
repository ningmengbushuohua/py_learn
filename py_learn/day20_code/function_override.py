# 函数的重写
# 函数重写的前提条件： 继承

# 1.自定义的函数重写
# 注意1: 如果子类未重写父类中的函数，则子类可以继承父类中的函数
#       如果子类重写了父类中的函数，子类对象将默认调用子类重写之后的函数
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
# 注意2:在子类函数重写函数的时候，如果仍然需要使用父类函数中的功能，则可以在子类函数中调用父类函数
class Brid(Animal):
    def style(self):
        super(Brid, self).style()
        # super().style()
        # Animal.style(self)
        print('flying')


d = Dog()
d.style()
c = Cat()
c.style()

f = Fish()
f.style()
b = Brid()
b.style()

print('*' * 44)
# 2.系统函数的重写
# 注意1:python 中所有类的父类是object,所以自定义的类默认使用系统功能继承自object
# a
class Person1(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person1('张三',56)
# 注意2. 当打印一个对象是，默认会调用系统的魔术方法，__str__, 该函数的返回值默认就是当前对象在内存中的地址
print(p1)   # <__main__.Person object at 0x000002615FA16E20>
print(p1.__str__())   # <__main__.Person object at 0x000002615FA16E20>

# b.__str__ : 返回当前对象的 字符串描述信息,返回值必须返回一个字符串
class Person2(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        # 注意： 必须返回一个字符串，一般情况下，返回当前对象相关的属性信息
        return f'姓名：{self.name},年龄：{self.age}'
    # def __repr__(self):
    #     return f'姓名：{self.name},年龄：{self.age}'
    __repr__ = __str__

p2 = Person2('张三', 56)
print(p2)       # 姓名：张三,年龄：56
print(p2.__str__())     # 姓名：张三,年龄：56

# 注意3； 将对象添加到容器中，直接打印容器，默认仍然显示地址，所以此时需要重写__repr__
lst = [p2]
print(lst)      # [姓名：张三,年龄：56]



# 3. 应用
import random
vip_info_list = []
class User():
    __slots__ = ('mid','name', 'age', 'sex')
    def __init__(self,mid,name,age,sex):
        self.mid = mid
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        return f'mid:{self.mid}, name:{self.name}'

    __repr__ = __str__

 # 会员管理系统类
class UserSystem():
    def __get_mid(self):
        while True:
            index = str(random.randint(10000, 99999))
            mid_tmp = (info.mid for info in vip_info_list)
            if index not in mid_tmp:
                return index

    def add_user(self,name, sex, age):
        index = self.__get_mid()
        print(f"会员{name}的会员编号是；{index}")
        # 创建对象
        user = User(index,name,age,sex)
        # 将对象添加到列表中
        vip_info_list.append(user)
        print(f'会员号为{index}的会员添加成功！')

    def del_user(self, index):
        # 将对象添加到列表中，从列表中遍历出来的也是对象，所以对象.属性就可以访问
        for info in vip_info_list:
            if info.mid == index:
                vip_info_list.remove(info)
                print(f'会员号为{index}的会员s删除成功！')
                break
        else:
            print(f'会员号为{index}的会员不存在！')

    def show_user(self, index):
        for info in vip_info_list:
            if info.mid == index:
                print(info)
                break
        else:
            print(f'会员号为{index}的会员不存在！')

    def sort_users(self):
        vip_info_list.sort(key=lambda x: x.age, reverse=True)
        print(vip_info_list)    # 目前打印对象，打印的结果是地址



# 调用函数
def main():
    print("欢迎登录会员信息管理系统".center(50, '*'))
    user_manage = UserSystem()
    while True:
        login_name = input("请输入登录用户信息")
        login_pwd = input("请输入登录密码")
        if login_pwd == 'admin' and login_name =='admin':
            print('登录成功')
            # 管理系统信息
            while True:
                print('''该系统中有如下功能：
                        1.添加会员信息
                        2.删除会员信息
                        3.查看会员信息
                        4.对会员信息进行降序排序
                        5.退出''')
                # 操作会员信息
                input_index_choice = input('请输入你需要操作的编号：')
                if input_index_choice == '1':
                    name = input('请输入会员姓名:')
                    sex = input('请输入会员性别:')
                    age = input('请输入会员年龄:')
                    user_manage.add_user(name,sex,int(age))
                elif input_index_choice == '2':
                    index = input("请输入需要删除的会员编号")
                    user_manage.del_user(index)
                elif input_index_choice == '3':
                    index = input("请输入需要查看的会员编号")
                    user_manage.show_user(index)
                elif input_index_choice == '4':
                    user_manage.sort_users()
                elif input_index_choice == '5':
                    print('欢迎再次使用')
                    break
                else:
                    print('无法识别，暂未开通此功能')
            break
        else:
            print('管理员信息输入有误，请重新输入')
main()
