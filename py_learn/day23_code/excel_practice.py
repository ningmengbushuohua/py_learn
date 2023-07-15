import openpyxl
# 1.打开已知的工作簿
wb = openpyxl.load_workbook(r'data/练习数据.xlsx')

# 获取工作表
sheet = wb.active
# 获取指定列的单元格对象
a_col = sheet['A']
# 整理数据
datalist = []
for cell in  a_col:
    data_temp = cell.value.split(';')
    for data in data_temp:
        datalist.append(data.strip().split(':'))
print(datalist)

# 写入到一个新的工作表
wb2 = openpyxl.Workbook()
sheet2 = wb2.active
sheet2.title = '处理结果'
sheet2.append(['日期','成交量'])
for data in datalist:
    sheet2.append(data)
wb2.save(r'data/练习数据-处理结果.xlsx')
