#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
# 1.randint(a,b)：步长固定为1，无法自定义，是一个闭区间
n1 = random.randint(1,10)
print(n1)

# 2.choice(seq):seq:序列,常用列表，元组或字符串 range()
n2 =random.choice([23,56,89,9,8])
print(n2)

n2 =random.choice((23,56,89,9,8))
print(n2)
n2 =random.choice('abck')
print(n2)
# range(start,end,step) ,生成一个容器，step默认为1 ，可以自定义， 是前闭后开区间
n2 =random.choice(range(100)) # 0-99
print(n2)
# 3.randrange(start,stop,step):step默认为1，可以自定义，是前闭后开区间
n3 = random.randrange(100)  # 0-99
print(n3)
n3 = random.randrange(1,100)  # 1-99
print(n3)
n3 = random.randrange(1,100,2)  # 1-99 获取奇数
print(n3)
# 练习：
# a. 获取20-90 之间的一个整数随机数
print(random.randint(20, 90))
print(random.choice(range(20, 91)))
print(random.randrange(20, 91))

# b. 获取 20- 90 之间的随意一个偶数随机数
print(random.choice(range(20, 91, 2)))
print(random.randrange(20, 91, 2))

# 4.sample(seq,k):从seq中随机获取k个数据，得到一个列表
print(random.sample([23,56,56,1,8,9,8], 2))
print(random.sample('ghjklfghjkdfghjkyuiortyuifghfjomqoakmn', 4))


# 5.random()：获取0~1之间的随机浮点数，前闭后开区间
n5 = random.random()
print(n5)
# 6.uniform(a,b):获取a~b之间的随机浮点数
# 工作原理 ：a + (b - a) * self.random()
n6 =random.uniform(10,59)
print(n6)

# 练习 ；求 20-100之间的随机数
print(random.uniform(20, 100))
# [0,1) ----->*80---> [0,80)----> +20 ---->[20,100)
print(20 + (100-20) * random.random())




