# with 上下文
# 推荐使用with
# 1.读取
with open(r'致青春.txt', 'r', encoding='utf-8') as f:
    r1 = f.readlines()
    print(r1)
# f.read()    # ValueError: I/O operation on closed file.

# 2. 写入
with open(r'aaa/file.txt', 'a', encoding='utf-8') as f1:
    f1.write('nihaohtttttt')
    f1.flush()


"""
语法：
with  对象   as  变量:
    pass

在文件读写中：
with  open()  as   f:
    读/写

说明：
    a.with上下文管理器一般用于简化代码，如：文件读写，数据库操作等
    b.使用with上下文管理器进行文件的读写之后，无需手动关闭文件，当with代码块执行完毕，对应的文件会自动关闭
    c.变量表示文件描述符，也就是打开的文件对象
    d.当通过with的方式打开文件，则文件读取和写入的操作一定要在with代码块中完成，否则文件会被关闭导致无法操作[ValueError: I/O operation on closed file.]
"""
