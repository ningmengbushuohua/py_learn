# 面向对象实例
import random
vip_info_list = []
# 一：封装函数
# 会员类
class User():
    __slots__ = ('mid','name', 'age', 'sex')
    def __init__(self,mid,name,age,sex):
        self.mid = mid
        self.name = name
        self.age = age
        self.sex = sex

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



# 二：调用函数
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