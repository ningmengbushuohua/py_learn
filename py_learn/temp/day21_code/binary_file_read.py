# 读取二进制文件
# 1.读取
# .因为二进制文件是由二进制【字节】组成，没有编码一说，所以需要省略encoding参数
    # ValueError: binary mode doesn't take an encoding argument
with open(r'aaa/img.png','rb') as f:
    data  = f.read()
    print(data)

# 2.写入
with open(r'aaa/pic.png','wb') as f:
    f.write(data)
    f.flush()
    