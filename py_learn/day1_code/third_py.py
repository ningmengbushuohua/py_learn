# 0.空行， 表示换行        *******
print()

# 1.输出单个数据
print(0)    # 整型
print("i love u")   # 字符串 str
print('i love u')   # 字符串 str
print(45.636)   #浮点型 float

# 2.输出多个数据
print(1, 2, 3, 5)
print(1, "ss", 25.36, 78, 'qaaa')

# 4.sep, 分隔符，默认值是空格
print(1, "ss", 25.36, 78, 'qaaa', sep='')
print(1, "ss", 25.36, 78, 'qaaa', sep='~')

# end :结束符，默认值 \n，表示是换行，也可以定义为其他
print(254, end='##')
print(598, end='^^')
print("789", end='***')
print(1, "ss", 25.36, 78, 'qaaa', end='##', sep='__')

