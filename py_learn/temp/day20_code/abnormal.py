# 异常的特点
print('start----')
num = int(input('请输入一个数字'))     # ValueError: invalid literal for int() with base 10: 'dsfs'
list1 = [32,4,32,5,5,7]
print(f'获取到的数字为 {list1[num]}')      # IndexError: list index out of range
print('end----')

# 异常最大的特点在于：当程序在执行的过程中，遇到了异常，且异常未被处理，则程序会终止异常处
# 处理异常的思想：将可能存在异常的代码监测起来，如果代码遇到异常，则跳过异常，继续执行后面的代码


