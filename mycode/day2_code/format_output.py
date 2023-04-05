#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# exmple day 1 : the information which input and output in console.
print('process is start!')

console_input_name = input("请输入姓名：")
console_input_age = input("请输入年龄：")
console_input_hobby = input("请输入爱好：")
print('我是', console_input_name, ',', '今年', console_input_age, ',','爱好',console_input_hobby, sep='')

print(f"我是{console_input_name},今年{console_input_age},爱好{console_input_hobby}")  # *****

print("我是%s,今年%s,爱好%s" %(console_input_name, console_input_age, console_input_hobby))

print('process is end!')