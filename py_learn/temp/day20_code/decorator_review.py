# 1. 装饰器 装饰函数
def wrapper(func):  # 参数命名;f/fun/func，表示需要被装饰的函数
    def inner():
        func()      # 调用原函数
        print('函数-----new')
    return inner
@wrapper        # 调用外部函数wrapper
def check():
    print('函数--check11-----')
check()     # 调用内部函数inner
print("*" * 87)

# 2.装饰器装饰类
def wrapper(cls):  # 参数命名;cls，需要被装饰的类
    def inner():
        print('类-----new')
        return cls()      # 创建对象
    return inner
@wrapper        # 调用外部函数wrapper
class Check():
    def __init__(self):
        print('init---类--check1----')
c = Check()     # 调用内部函数inner
print(c)