'''
1.邮编查询，读取 youbian.txt 文件中的数据， 完成邮编查询的操作，从控制台输入邮编号，如果有此邮编，请输出对应的城市，否则提示无此邮编
2.将一个英文语句以单词为单位逆序排放到指定的文件中
    例如：“I am a boy” 逆序排放后 "boy a am I" 将其写入到指定的文件中
3.开房查询，从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中

'''

# def get_city(youbian):
#     with open(r'data/youbian.txt','r',encoding='utf-8') as f:
#         result = f.readlines()
#         print(result)
#         for r in result:
#             if youbian == r[1:7]:
#                 print(r)
#                 print(f'所查询的城市是{r[9:-4]}')
#                 break
#         else:
#             print('暂无此邮编')
#
# def get_city2(code):
#     with open(r'data/youbian.txt',"r",encoding="utf-8") as f:
#         data_list = f.readlines()
#         print(data_list)
#     for data in data_list:
#         info_list = eval(data.rstrip(",\n"))
#         if str(info_list[0]) == code:
#             # print(info_list,type(info_list))
#             print(f"{code}存在，对应的城市为:{info_list[1]}")
#             break
#     else:
#         print(f"{code}不存在")
# if __name__ == '__main__':
#     youbian = input("请输入需要查询的城市的邮编号：")
#     get_city2(youbian)

#   2.
# english_str = 'I am a Boy'
# new_en_str = ' '.join((english_str.split(' ')[::-1]))
# with open(r'data/temp.txt','w',encoding='utf-8') as f:
#     f.write(new_en_str)
#     f.flush()

# 3.
name = input('请输入需要查询的名字')
def read_data():
    with open(r'data/kaifanglist.txt', 'r', encoding='utf-8') as f:
        result = f.readlines()
    return result
def search_data(name):
    infos = read_data()
    single_list = []
    for info in infos:
        infolist = info.split(',')
        if infolist[0] == name:
            single_list.append(info)
    write_data(single_list,name)

def write_data(single_list,name):
    if single_list:
        print(f'{name}有开房记录')
        des_path = f'data/{name}.txt'
        with open(des_path,'w',encoding='utf-8') as f:
            for line in single_list:
                f.write(line)
                f.flush()
        print('信息提取成功')
    else:
        print('暂无数据')

if __name__ == '__main__':
    name = input("请输入需要查询的人员的姓名：")
    search_data(name)
