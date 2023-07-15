# 读取普通文件
# 1.打开文件：open()
'''
注意:
    a.传递需要读取的文件的路径
        绝对路径
        相对路径，当前的工程中【day21_code】中和当前py 文件的相对路径，推荐使用
    b.打开文件的模式 'r' ，open for reading (default)
    c. endocing: 需要读取的文件的编码格式,注意需要使用关键字参数
    d:f = open(), f 表示被打开的文件对象，后续操作需要使用f对象完成

'''
# f1 = open(r'D:\work\temp\致青春1.txt')        # 绝对路径

# 情况一: 如果py文件和 txt 文件平级， 直接写txt文件名字
# f1 = open(r'致青春.txt')       # 相对路径
# 情况二
# f2 = open(r'data\致青春1.txt')     #也可以是data/致青春1.txt   /；斜杠  \：反斜杠

f = open(r'致青春.txt', 'r', encoding='utf-8')

# 2.写入内容,read()/readline()/readlines()
# 一次读取全部读取完毕，适用于数据量少的文件
# r1 = f.read()
# print(r1)
# 一次只能读取一行
# r2 = f.readline()
# print(r2)
# 一次性全部读完，同样适用于数据量小的情况，但是返回列表，每一行是列表中的元素,使用较多
r3 = f.readlines()
print(r3)

# 3.关闭文件close()
# 关闭文件，为了节约内存空间
f.close()

# 扩展: 结合异常读取文件
# FileNotFoundError
# ValueError
# LookupError

f1 = None
try:
    f1 = open(r'致青春.txt', 'r', encoding='utf-8')
    print(f1.read())
except FileNotFoundError as e:
    print('文件路径错误：',e)
except ValueError as e:
    print('打开模式错误：',e)
except LookupError as e:
    print('编码错误：',e)
finally:
    if f1:
        f1.close()
