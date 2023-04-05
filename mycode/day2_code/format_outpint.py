#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# exmple day 1 : the information which input and output in console.
print('process is start!')

# console_input_name = input("请输入姓名：")
# console_input_age = input("请输入年龄：")
# console_input_hobby = input("请输入爱好：")
console_input_name= 400
console_input_age= 18
console_input_hobby='吃饭'

print(console_input_name, console_input_age, console_input_hobby, sep=',')

# 占位符： “指定格式的占位符” % (实际的数据)
# 注意1， 占位符数量和实际数据数量需要一致
# 注意2， 占位符数量和实际数据的类型需要一致
# 注意3， %.nd,n大于等于1， 表示整型的格式化
# 注意4， %.nf,n大于等于1， 表示浮点型的格式化，  不加n，默认小数点后补全6位
print('信息1：%d, 信息2：%d, 信息3:%s' % (console_input_name,console_input_age,console_input_hobby))


print('信息1：%.6d, 信息2：%d, 信息3:%s' % (console_input_name,console_input_age,console_input_hobby))

print('年龄：%.3f' %(18.5659))

# 占位符  f”“/ f-string
print(f"信息1：{0.5},信息2:{589}, 信息3：{'sss'}")

print(f"体重：{150.66666:.3f}")
print('process is end!')


