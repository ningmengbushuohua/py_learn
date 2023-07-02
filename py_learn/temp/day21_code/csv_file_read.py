# csv 文件的读取
# xxx.txt  xxx.csv

# 注意1. csv 文件的读写较为特殊，所以需要借助于系统模块csv
import csv
# 1. 读取
# 注意5：如果写入内容之后，每行后面出现了空行，则可以通过设置newline=''解决
with open(r'aaa/file_csv.csv','r',encoding='utf-8') as f1:
    #注意2.读取csv文件时，使用csv.reader(),返回迭代器
    reader = csv.reader(f1)     # 相当于f1.read()
    print(reader)       # <_csv.reader object at 0x000001B176898D00>
    # for r in reader:
    #     print(r)
    datalist = list(reader)
    print(datalist)

# 2. 写入
with open(r'aaa/t2.csv','w',encoding='utf-8',newline='') as f2:
    # 注意3. 写入csv文件时，使用csv.writer(),结合使用writerow() 或者writerows()完成写入操作
    writer = csv.writer(f2)
    # 注意4：writerow(可迭代对象) 或者writerows(可迭代对象)
    # writer.writerow('hello')
    datalist = [['name', 'age', 'height', 'address'],
                ['张三', '23', '124', '上海'],
                ['张四', '23', '174', '杭州'],
                ['张五', '23', '184', '上海']]
    # 逐行写入
    # for data in datalist:
    #     writer.writerow(data)

    # 一次性写入多行
    writer.writerows(datalist)