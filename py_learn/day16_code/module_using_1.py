#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.系统模块：python中自带的模块，可以直接导入使用
# 【面试题】 列举python 中系统常用的模块
import random
# random.randint(2,78)
import math
import time
import re
import string
import functools

# 2.自定义模块：自己封装一个模块：该模块中实现了某些特定的功能
# 注意1: 实际上一个 .py文件就是一个模块。 py文件的文件名相当于模块名，
#       所以一个合法的模块必须要遵守标识符的规则和规范
# 注意2: 包：本质是一个文件夹，但是区别于普通的文件夹，其中包含一个__init__.py 文件
# 注意3： 包的存在和文件夹的存在，原理是一样的，都是为了管理文件
# 注意4： 在导入自定义模块时，需要注意模块的路径问题,需要将模块所在的包或者文件夹声明，所以需要使用相对路径表示
# 注意5: 书写自定义模块，格式 xxx.xxx.xxx。不管是包还是文件夹，用法完全相同
# import temp_pack.tmp0
# import temp_pack1.tmp1
# import temp_pack2.tmp_pack.tmp2

# 3.import xxx
# a.
# import random,math,string
# import temp_pack.tmp0
# import temp_pack1.tmp1
# import temp_pack2.tmp_pack.tmp2
#
# # 语法： 模块名.函数/变量
# r1 = random.choice('sssqq')
# r2 = random.sample('2332536', 2)
#
# print(temp_pack.tmp0.name0)
# temp_pack.tmp0.func0()
#
# print(temp_pack2.tmp_pack.tmp2.name2)
# temp_pack2.tmp_pack.tmp2.func2()

# b. import xxx as xx
import random as r
import temp_pack.tmp0 as t0
import temp_pack1.tmp1 as t1
import temp_pack2.tmp_pack.tmp2 as t2

# 语法： 模块名.函数/变量
r1 = r.choice('sssqq')
r2 = r.sample('2332536', 2)

print(t0.name0)
t0.func0()

print(t2.name2)
t2.func2()

# 应用 ：在后期数据分析三剑客
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt