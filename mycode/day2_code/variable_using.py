#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 变量重新赋值
name = 'sss'    # 初始值
print(name)
name = '989s'   # 重新赋的值
print(name)

# 2. id(x) ：数据在计算机内存的地址
# 获取一个变量的地址， 实际是获取变量中存储的数据的地址   # ********
jax= 'jaax'

print(id(jax))
print(id('jax'))

# 3. type(x): 获取数据的 数据类型
va1 = 66    # <class 'int'>
va2 = None  # <class 'NoneType'>
print(type(va1))
print(type(va2))

# 注意：  但凡是通过input 从控制台输入的数据，都是字符串类型
age:int = input("请输入年龄")
print(type(age))
print(age)

# 4. 常量
# 注意： 程序中，一个变量表示的值不需要被修改， 将它定义为常量
# 变量 所有字母全部小写， 不同单词之间使用下换线
# 常量 所有字母全部大写， 不同单词之间使用下换线
PI = 3.152
print(PI)

PI = "2656"
print(PI)