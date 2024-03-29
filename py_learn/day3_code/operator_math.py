#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#注意：
    # 1. 浮点数参与运算，结果都是浮点数
    # 2. 只要是除法运算 ，结果都是浮点数
    # 3. // 的结果是 /的整数部分
    # 4. 算术运算符   **  */  +-

# 1. + -
print(2 + 6 )
print(10 - 4)
print(2.0 + 6)  # 8.0
print(2 + 6.0)  # 8.0
print(2.0 + 6.0)    # 8.0


# 2. * /
print(2 * 6 )
print(10 / 4)
print(2.0 * 6)  #
print(2 * 6.0)  #
print(2.0 * 6.0)    #

# 3.// :整除
print(5/3)  # 1.6667
print(5//3) # 1
print(5.0//3) # 1.0

# 4.%:求余或取模
print(5 % 3)    # 2
print(5.0 % 3)    # 2.0
print(5.00 % 3)    # 2.0   看是不是 浮点数
print(10 % 2)    # 0

# 5. ** ：次方
print(5 ** 3)
print(2 ** 10)
print(2.0 ** 10)

# 6. 优先级问题
print(2 * 10 ** 3) # 2000
# 提高运算符优先级
print((2 * 10) ** 3)  # 20 ** 3   8000


