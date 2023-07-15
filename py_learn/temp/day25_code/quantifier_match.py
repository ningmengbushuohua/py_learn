# 数量词匹配
import re

# 1.
'''
x{n}     匹配确定的n个x（n是一个非负整数）
x{n,}    匹配至少n个x
x{n,m}   匹配至少n个最多m个x。注意：n <= m
'''
# match对象.group(): 获取匹配到的字符串
r1 = re.match(r'\d{3}', '523252')
print(r1.group())       # 523
r1 = re.match(r'\d{3,}', '5232523124124a353543')
print(r1.group())       # 5232523124124   尽可能多的匹配
r1 = re.match(r'\d{3,5}', '52325243')
print(r1.group())       # 52325

# 需求：匹配一个四位的验证码，每一位都由数字或者字母组成
# r1 = re.match(r'[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]','3234')
# print(r1)
r1 = re.match(r'[a-zA-Z0-9]{4}','3234')
print(r1)

# 2.
"""
x?       匹配0个或者1个x
x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
x+       匹配1个 或者 多个

"""
r1 = re.match(r'\d?', '5232523242')
print(r1.group())       # 5
r1 = re.match(r'\d+', '5232523124124a353543')
print(r1.group())       # 5232523124124   尽可能多的匹配
r1 = re.match(r'\d*', '5232523124124a353543')
print(r1.group())       # 5232523124124


# 3. match() 和search() 和 finall() 的区别
'''
match():匹配，从左往右依次匹配，如果匹配上，返回Match对象，如果匹配不上，返回None    # 必须从左往右
search():搜索，底层和match的使用相同，如果搜索到，返回Match对象，如果搜索不上，返回None
	注意：只要搜索到一个符合条件的子字符串，则停止搜索
findall():查找所有，最终的结果返回一个列表
'''
r1 = re.match(r'\d+', 'az523252yret3124124a353wr543')
print(r1)       # None

r1 = re.search(r'\d+', 'za523252yret3124124a353wr543')
print(r1)       # <re.Match object; span=(2, 8), match='523252'>

r1 = re.findall(r'\d+', 'az523252yret3124124a353wr543')     # *********
print(r1)               # ['523252', '3124124', '353', '543']
