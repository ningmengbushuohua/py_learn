# 边界匹配
import re
# 1.
"""
^     行首匹配，和在[]里的^不是一个意思
$     行尾匹配
"""
# 注意： 默认情况下，字符串使用的是单行模式，哪怕字符串中包含 \n 换行符
r1 = re.findall(r'^this', 'this is my love\nthis my home\nthis is my pc')
print(r1)       # ['this']
r1 = re.findall(r'love$', 'this is my love\nthis my home\nthis is my love')
print(r1)       # ['love']

# 注意：如果需要匹配多行的行首或者行尾，则需要设置flags= re.M 或者 flags= re.MULTILINE，
#       才表示多行模式
r1 = re.findall(r'^this', 'this is my love\nthis my home\nthis is my pc', flags= re.M)
print(r1)           # ['this', 'this', 'this']
r1 = re.findall(r'love$', 'this is my love\nthis my home\nthis is my love', flags= re.MULTILINE)
print(r1)           # ['love', 'love']


# **********  $ ：经常用于位数的限制中
qq = '766753452424254211111'
r = re.match(r'[1-9]\d{4,10}$', qq)    # [1-9][0-9]{4,10}
print(r)

# 2.
'''
\A    匹配字符串开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z    匹配字符串结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾
'''
r1 = re.findall(r'\Athis', 'this is my love\nthis my home\nthis is my pc')
print(r1)       # ['this']
r1 = re.findall(r'love\Z', 'this is my love\nthis my home\nthis is my love')
print(r1)       # ['love']

# 注意：如果需要匹配多行的行首或者行尾，则需要设置flags= re.M 或者 flags= re.MULTILINE，
#       才表示多行模式
r1 = re.findall(r'\Athis', 'this is my love\nthis my home\nthis is my pc', flags= re.M)
print(r1)           # ['this']
r1 = re.findall(r'love\Z', 'this is my love\nthis my home\nthis is my love', flags= re.MULTILINE)
print(r1)           # ['love']