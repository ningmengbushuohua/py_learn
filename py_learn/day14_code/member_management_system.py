#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
根据下面的需求描述，完成简单的用户管理系统，注意封装函数

1. 后台管理员只有一个用户: admin, 密码: admin
2. 当管理员登陆账号成功后， 可以管理前台会员信息.
3. 会员信息管理包含方法:
   a.添加会员信息
   b.删除会员信息
   c.查看会员信息
4. 对会员按照年龄降序排序
5. 退出

思路：
    1.输入用户名和密码 跟 管理员的账号密码匹配 不一致的话 登陆失败
    一致的话 提示登陆成功
    并列出 对应的 1 2 3 4 5的操作 输入对应的编号 执行对应的方法

    2.会员信息包含：
            会员编号(mid) ---- 编号是在10000到99999中随机选择一个 不能重复
            会员姓名(name)
            会员性别(sex)
            会员年龄(age)
            使用字典保存每个会员信息
                    例如{'mid':10000, 'name':'乐乐','sex':'男', 'age':20}
            使用列表保存所有的会员
                例如[{'mid':10000, 'name':'乐乐','sex':'男', 'age':20},{'mid':10001, 'name':'美美','sex':'女', 'age':19}]
'''

# 一:封装函数
import random
vip_info_list = [{'mid':'10000', 'name':'乐乐','sex':'男', 'age':20},{'mid':'10001', 'name':'美美','sex':'女', 'age':19}]

def get_mid():
    while True:
        index = str(random.randint(10000, 99999))
        mid_tmp = (info['mid'] for info in vip_info_list)
        if index not in mid_tmp:
            return index
def add_user(name,sex,age):
    index = get_mid()
    print(f"会员{name}的会员编号是；{index}")
    vip_info_list.append(dict(zip(['mid', 'name', 'gender', 'age'], [index, name, sex, age])))
    print(f'会员号为{index}的会员添加成功！')
def del_user(index):
    for info  in vip_info_list:
        if info['mid'] == index:
            vip_info_list.remove(info)
            print(f'会员号为{index}的会员s删除成功！')
            break
    else:
        print(f'会员号为{index}的会员不存在！')
def show_user(index):
    for info in vip_info_list:
        if info['mid'] == index:
            print(info)
            break
    else:
        print(f'会员号为{index}的会员不存在！')
def sort_users():
    vip_info_list.sort(key=lambda x: x['age'], reverse=True)
    print(vip_info_list)

# 二：调用函数
def main():
    print("欢迎登录会员信息管理系统".center(50, '*'))
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
                    add_user(name,sex,int(age))
                elif input_index_choice == '2':
                    index = input("请输入需要删除的会员编号")
                    del_user(index)
                elif input_index_choice == '3':
                    index = input("请输入需要查看的会员编号")
                    show_user(index)
                elif input_index_choice == '4':
                    sort_users()
                elif input_index_choice == '5':
                    print('欢迎再次使用')
                    break
                else:
                    print('无法识别，暂未开通此功能')
            break
        else:
            print('管理员信息输入有误，请重新输入')
main()

