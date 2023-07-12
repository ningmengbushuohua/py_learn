# json 模块
# json 模块提供了序列化和反序列化的方法
# 序列化： 将字符串转为字典
# 反序列化： 将字典转为字符串

import json
# 1.json.loads(): 将字符串类型的json 数据转为字典
json_str ='''{
  "name": "JSON数据",
  "age": 23,
  "total_score": 365,
  "level_A": true,
  "address": null,
  "family": ["爸爸","妈妈","爷爷"],
  "desc": "整个JSON数据就是一个对象（使用{}括起来的部分）",
  "scores": {"语文": 65,"数学": 78,"英语": 60.8}
}
'''
print(type(json_str))
data = json.loads(json_str)
print(data,type(data))

# 2. json.dumps(): 将字典转为 字符串的json 数据
new_json_str = json.dumps(data, ensure_ascii=False)
print(new_json_str, type(new_json_str))

# json 数据中的汉字在传输时都会变成十六进制， 这样传输才能更高效