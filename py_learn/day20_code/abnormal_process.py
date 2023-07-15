print('start----')
# 出现异常：抛出异常
# 处理错误：捕获异常
try:
    # 可能存在异常的代码
    num = int(input('请输入一个数字'))
    list1 = [32,4,32,5,5,7]
    print(f'获取到的数字为 {list1[num]}')
except ValueError as e:
    # e: 异常的描述信息
    print('ValueError', e)
except IndexError as e:
    print('IndexError', e)
finally:
    # 任何情况下都会执行，一般进行文件的关闭，或者数据库的关闭
    print('finally')
print('end----')