# xlrd 读取xls

# 1.库的划分
# import random,math,string   # 系统模块，系统库
# import module   # 自定义模块、自定义库
# import xlrd,xlwt,openpyxl  # 第三方库、第三方模块

# 2. 读取xls 格式的Excel 文件
import xlrd

# a.打开Excel 文件，得到一个工作簿对象
wb = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')
print(wb)

# b.获取工作簿中工作表名称
sheet_names = wb.sheet_names()
print(sheet_names)  # ['会员信息表']

# c.获取工作表对象
# 1> 根据工作表名称获取对象
sheet1 = wb.sheet_by_name('会员信息表')
print(sheet1)
# 2> 根据索引获取对象
sheet_1 = wb.sheet_by_index(0)
print(sheet_1)


# d.获取单元格 对象
# sheet1.cell(row,col)
cell1 = sheet1.cell(0,0)    # A1
print(cell1,type(cell1))        # text:'Date' <class 'xlrd.sheet.Cell'>
cell2 = sheet1.cell(0,2)    # C1
print(cell2)                    # text:'Low'

# e.获取单元格中的值
# 1>先获取单元格的对象，通过value属性访问单元格的值
cell1 = sheet1.cell(0,0)
print(cell1.value,type(cell1.value))    # Date <class 'str'>
# 2>sheet.cell_value(row,col)
v = sheet1.cell_value(0,2)
print(v,type(v))        # Low <class 'str'>

# f.获取某行的某几列的数据，
# sheet.row_values(row,col1,col2): col2 不包含在内，返回一个列表，其中元素是字符串
print(sheet1.row_values(0))     # 获取第0行的数据  ['Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
print(sheet1.row_values(0,0,2))     # # 获取第0行的第0-1列     ['Date', 'High']

# sheet.row_slice(row,col1,col2): col2 不包含在内，返回一个列表，其中元素是单元格对象
print(sheet1.row_slice(0))     # 获取第0行的数据   # [text:'Date', text:'High', text:'Low', text:'Open', text:'Close', text:'Volume', text:'Adj Close']
print(sheet1.row_slice(0,0,2))     # # 获取第0行的第0-1列  # [text:'Date', text:'High']
