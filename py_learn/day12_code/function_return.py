#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.返回值的意义
# 定义
def f1():
    num1 = 10
# 调用
f1()
# 注意： 在函数内部定义的变量， 只能在当前函数的内部的代码块中被访问
# print(num1)     # NameError: name 'num1' is not defined

# 注意2:在函数内部定义的变量，如果需要在函数外面的访问，则可以通过设置返回值的方式
# 注意3： 在哪里调用函数，则返回值会返回到哪里
def f2():
    print('start---')
    num2 = 66
    return num2
r2 = f2()
print(r2)

print(f2())     # 相当于调用了函数，同时打印了该函数的返回值

# 2.未设置返回值
# a.如果一个函数未设置返回值，默认的返回值是None(空值)
def fun1():
    print('11111')
r1 = fun1()
print(r1)   # None,  remove()/ append():None

# 3. return: 返回，只能使用在函数中，可以单独作为一条语句，表示结束函数
# 注意4： 如果函数中出现return，当执行到return 时，函数直接结束，所以和
#         所以和return平级的情况下，return后面不书写任何语句，因为这些语句没有执行的机会
def func2():
    print('22222')
    return
    # print('over-----')
func2()

# 4.return xxxx:既表示结束函数，也表示将xxx数据返回
def fun3():
    print('3333')
    return "abc"
r3 = fun3()
print(r3)

# 注意5:如果return后面返回多个数据，则最终结果是一个元组
def fun33():
    print('3333')
    return "abc",'4',4,5,6
r31 = fun33()
print(r31)      # ('abc', '4', 4, 5, 6) 打包

# 注意6： 如果函数中有if，while, for等语句，不平级的情况下，return 的后面
# 是可以书写其他语句的，但是该语句不一定有机会执行。
def fun32(n):
    print('33333---')
    if n > 10:
        return 111
    print('over---')
r11 = fun32(4)
print(r11)
r11 = fun32(54)
print(r11)

# 注意7：在同一函数中，根据分支语句的执行，可以书写多个return
# 如果使用的是双分支，可以省略else
def fun32(n):
    print('33333---')
    if n > 10:
        return 111
    else:
        return 222
r32 = fun32(6)
print(r32)
r32 = fun32(18)
print(r32)

# 等价于上面的代码
def fun33(n):
    print('33333---')
    if n > 10:
        return 111
    return 222

# 5. break 和return的区别       ********
'''
break：使用在循环中，表示结束当前循环
return; 使用在函数中，表示结束当前函数，
    不论return存在于多少层循环中，只要执行到return，函数立马结束掉
'''
# a.
def c1():
    print('start----')
    for i in range(3):
        for j in range(5):
            print(i,j)
            if j == 1:
                break
    print('end---')
c1()

# b.
def c2():
    print('start----')
    for i in range(3):
        for j in range(5):
            print(i,j)
            if j == 1:
                return      # 直接结束该函数，不论在多少层循环内，end 不会打印
    print('end---')
c2()

