'''
常见异常
【面试题】列出Python中常见的异常，至少5种
AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
'''

# 1. NameError 使用一个还未被赋值的变量
# print(num)      # NameError: name 'num' is not defined

# 2. ValueError 传入一个调用者不期望的值，即使值的类型是正确的
# num = int(input('请输入一个数字：'))    # ValueError: invalid literal for int() with base 10: 'nj'

# 3. TypeError 传入对象类型与要求不符合
# print(10 + 'gfdgds')        # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 4.IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# numlist = [23,52,2]
# print(numlist[100])     # IndexError: list index out of range

# 5.AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
# 'abc'.reverse()     # AttributeError: 'str' object has no attribute 'reverse'

# 6.ModuleNotFoundError: 模块导入错误，一般是模块的路径或者模块书写错误
# import rand     # ModuleNotFoundError: No module named 'rand'

# 7.FileNotFoundError :文件路径错误

# 8.UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# a = 43
# def func():
      # 不同作用域重名变量产生冲突的问题。
#     a += 1      # UnboundLocalError: local variable 'a' referenced before assignment
# func()