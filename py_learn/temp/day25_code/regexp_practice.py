# 正则练习
import re
"""
1.用户名匹配
			要求:	1.用户名只能包含数字 字母 下划线
					2.不能以数字开头
					3.⻓度在 6 到 16 位范围内
"""
def check_username(username:str):
    r = re.match(r'[^0-9]\w{5,15}$',username)
    return True if r else False

"""
2.密码匹配 

			要求:	1.不能包含!@#¥%^&*这些特殊符号
					2.必须以字母开头 
					3.⻓度在 6 到 12 位范围内
"""
def check_pwd(pwd):
    r = re.match(r'[a-zA-Z][^!@#¥%^&*]{5,11}$',pwd)
    return True if r else False

# 3.将给定字符串中的数字挑出，拼接成一个新的字符串
def get_num(data):
    # 方式一：
    # +: 一位或者多位
    r = re.findall(r'\d+',data)
    code = ''.join(r)
    print(code)

    # 方式二
    r = re.split(r'\D+',data)
    code = ''.join(r)
    print(code)
get_num('q3qrqwer3241412bfghe')

# 4.将给定字符串中的数字挑出，求和
def get_num_sum(data):
    # 方式一：
    # +: 一位或者多位
    r = re.findall(r'\d+',data)
    total = sum([int(num) for num in r])
    print(total)

    # 方式二
    r = re.split(r'\D+',data)
    total2 = sum([int(num) for num in r if num != ''])
    print(total2)
get_num_sum('q3qrqwer3241412bfghe')