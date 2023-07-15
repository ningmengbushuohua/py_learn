# 分组匹配
"""
x|y      |表示或，匹配的是x或y
(xyz)    匹配小括号内的xyz(作为一个整体去匹配)
"""


# 1.
import re
print(re.findall(r'\d+','sds23224345--qreqca42431231'))
print(re.findall(r'[a-z]+','sds23224345--qreqca42431231'))
'''
['23224345', '42431231']
['sds', 'qreqca']
'''

# 2.
print(re.findall(r'\d+|[a-z]+','sds23224345--qreqca42431231'))
'''
['sds', '23224345', 'qreqca', '42431231']
'''

# 3.
print(re.findall(r'(\d+)|[a-z]+','sds23224345--qreqca42431231'))
# ['', '23224345', '', '42431231']
print(re.findall(r'\d+|([a-z]+)','sds23224345--qreqca42431231'))
# ['sds', '', 'qreqca', '']

# 4.捕获型分组
# 只显示()，中的内容
print(re.findall(r'(\d+)|[a-z]+','sds23224345--qreqca42431231'))
# ['', '23224345', '', '42431231']
print(re.findall(r'\d+|([a-z]+)','sds23224345--qreqca42431231'))
# ['sds', '', 'qreqca', '']
print(re.findall(r'(\d+)|([a-z]+)','sds23224345--qreqca42431231'))
# [('', 'sds'), ('23224345', ''), ('', 'qreqca'), ('42431231', '')]
print('*' * 87)

# 5. 非捕获型分组
# (?:xxxx)
print(re.findall(r'(?:\d+)|[a-z]+','sds23224345--qreqca42431231'))
# ['sds', '23224345', 'qreqca', '42431231']
print(re.findall(r'\d+|(?:[a-z]+)','sds23224345--qreqca42431231'))
# ['sds', '23224345', 'qreqca', '42431231']

# 6. finditer(): 区别于finall,返回迭代器, 没有加括号的捕获型分组的问题
r1 = re.finditer(r'(\d+)|[a-z]+','sds23224345--qreqca42431231')
print(r1)
# print(list(r1))
print([ele.group() for ele in r1])

r2 = re.finditer(r'\d+|([a-z]+)','sds23224345--qreqca42431231')
print(r2)
# print(list(r2))
print([ele.group() for ele in r2])
