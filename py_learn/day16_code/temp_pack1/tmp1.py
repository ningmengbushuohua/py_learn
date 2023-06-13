#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('start~~~~~')
name1 = 11
def func1():
    print(name1)

name11 =111
def func11():
    print(name11)

# __name__:系统变量，用于获取模块名，如果运行的是当前文文件，则值为__main__
print(__name__)
print('end~~~~~')

# __name__ =='__main__',可以用来判断正在运行的是否是当前模块文件
# 如果if中的代码执行，则说明运行的是当前文件，如果if中的代码不执行，则表示运行的是其他文件，当前文件是被导入使用
if __name__ == '__main__':
    print('if语句中的代码被执行了',name1,name11)
    func1()
    func11()

