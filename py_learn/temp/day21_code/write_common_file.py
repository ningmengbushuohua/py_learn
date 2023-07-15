# 1.打开文件
'''
注意：
    a.写入文件内容【w或者a】的时候， 文件路径可以不存在，自动生成
    b.不管是读取还是写入，enconding的值和源文件的编码格式保持一致
    c.
        'w':open for writing, truncating(删除) the file first,  达到了覆盖的效果
        'a'：open for writing, appending to the end of the file if it exists,达到追加内容的效果

'''
# f1 = open(r'/aaa/file.txt','w',encoding='utf-8')        # 文件路径存在
# f1 = open(r'aaa/file2.txt','w',encoding='utf-8')        # 文件路径不存在，自动创建
f1 = open(r'aaa/file.txt','w',encoding='utf-8')
fr = open(r'致青春.txt','r',encoding='utf-8')
# 2. 写入内容
f1.write(fr.read())
# 如果需要写入的数据量较大，则可以借助刷新提高写入效率
f1.flush()
# 3. 关闭文件
f1.close()
fr.close()
