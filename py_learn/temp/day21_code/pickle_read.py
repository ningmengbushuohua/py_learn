# 对象的写入
# with open('aaa/a1.txt','w',encoding='utf-8') as f:
#     f.read([43,432,1])  # TypeError: argument should be integer or None, not 'list'

import pickle
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'姓名，{self.name}年龄：{self.age}')
p1 = Person('张三',23)
# with open('aaa/a1.txt','w',encoding='utf-8') as f:
#     f.write(p1)     # TypeError: write() argument must be str, not Person

# 1. 序列化【写入】
# 注意; 需要pickle序列化对象，则文件的打开方式一定要使用wb 或者rb,类似于二进制文件的读写
with open('aaa/a1.txt','wb') as f:
    pickle.dump(p1,f)   # pickle.dump(写入的对象，文件对象)

# 2. 反序列化【读取】
with open('aaa/a1.txt','rb') as f:
    r = pickle.load(f)      # pickel.load(文件对象)
    print(r)
    print(r.name,r.age)
    r.show()