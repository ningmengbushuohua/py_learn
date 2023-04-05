#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.打印0-9
n = 0   # 0 相当于 range() start
while n< 10:    # 9 相当于 range() end
    print(n)
    n += 1      # 9 相当于 range() step

for n in range(0, 10):  # range(0, 10 , 1)
    print(n)

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 打印 1- 100的 和
n = 1
total = 0   # 用于求和的变量，初始值 0
while n< 101:
    total += n
    n += 1
print(total)

total = 0
for n in range(1,101):
    total += n
print(total)

# 3. 统计1- 100之间3的倍数
m = 1
times = 0
while m <101:
    if m % 3 ==0:
        times += 1
    m += 1
print(times)

times = 0
for i in range(1, 101):
    if i % 3 == 0:
        times += 1
print(times)


m = 3
times = 0
while m <101:
    times += 1
    m += 3
print(times)

times = 0
for i in range(3, 101, 3):
    times += 1
print(times)