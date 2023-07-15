# 贪婪匹配和非贪婪匹配
import re
"""
非贪婪匹配：
x?       匹配0个或者1个x

贪婪匹配：
x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
x+       匹配1个 或者 多个

"""
# 1.
r1 = re.match(r'\d?', '5232523124124353543')
print(r1.group())       # 5
r1 = re.match(r'\d+', '5232523124124353543')
print(r1.group())       # 5232523124124353543   尽可能多的匹配
r1 = re.match(r'\d*', '5232523124124353543')
print(r1.group())       # 5232523124124353543

# 2.
print(re.findall(r's\w','sds23224345__qreqca42431231h'))
print(re.findall(r'\wh','sds23224345__qreqca42431231h'))
print(re.findall(r's\wh','sds23224345__qreqca42431231h'))
'''
['sd', 's2']
['1h']
[]
'''

print(re.findall(r's\w?','sds23224345__qreqca42431231h'))
print(re.findall(r'\w?h','sds23224345__qreqca42431231h'))
print(re.findall(r's\w?h','sds23224345__qreqca42431231h'))
'''
['sd', 's2']
['1h']
[]
'''

print(re.findall(r's\w+','sds2322434h5_qreqcah42431231h'))
print(re.findall(r'\w+h','sds2322434h5_qreqcah42431231h'))
print(re.findall(r's\w+h','sds2322434h5_qreqcah42431231h'))
'''
['sds2322434h5_qreqcah42431231h']
['sds2322434h5_qreqcah42431231h']
['sds2322434h5_qreqcah42431231h']
'''

print(re.findall(r's\w*','sds2322434h5_qreqcah42431231h'))
print(re.findall(r'\w*h','sds2322434h5_qreqcah42431231h'))
print(re.findall(r's\w*h','sds2322434h5_qreqcah42431231h'))
'''
['sds2322434h5_qreqcah42431231h']
['sds2322434h5_qreqcah42431231h']
['sds2322434h5_qreqcah42431231h']
'''
print('*' * 78)

print(re.findall(r's\w*?','sds2322434h5_qreqcah42431231h'))
print(re.findall(r'\w*?h','sds2322434h5_qreqcah42431231h'))
print(re.findall(r's\w*?h','sds2322434h5_qreqcah42431231h'))
'''
['s', 's']
['sds2322434h', '5_qreqcah', '42431231h']
['sds2322434h']
'''

print(re.findall(r's\w+?','sds2322434h5_qreqcah42431231h'))
print(re.findall(r'\w+?h','sds2322434h5_qreqcah42431231h'))
print(re.findall(r's\w+?h','sds2322434h5_qreqcah42431231h'))
'''
['sd', 's2']
['sds2322434h', '5_qreqcah', '42431231h']
['sds2322434h']
'''

# +?  或者 *?  将原本的贪婪匹配转换为非贪婪匹配