#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. from xxx import xxx
# a.from 模块名 import 函数名/变量/类

# 语法：函数/变量
from random import choice,randint,sample
from temp_pack.tmp0 import name0,func0
from temp_pack2.tmp_pack.tmp2 import name2,func2

r1 = choice('xxxswfs')
func0()

print(name2)
func2()

# b.from 模块名 import *
# 注意： * 表示所以
from temp_pack1.tmp1 import *
print(name1)
func1()
func11()
