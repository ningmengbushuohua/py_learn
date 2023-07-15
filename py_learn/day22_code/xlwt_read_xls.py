# xlwt  写入xls
import xlwt

# Excel 文件不存在，创建新的文件

# 1. 创建一个空的工作簿对象
wb = xlwt.Workbook()
# 2.向工作簿中添加工作表，返回添加的工作表对象
sheet = wb.add_sheet('学生表')
# 3. 向工作表中写入数据
# sheet.write(row,col,value)

# sheet.write(0,0,'name')
# sheet.write(0,1,'age')
# sheet.write(0,2,'sex')

titlelist = ['name','age','sex','score']
for i in range(len(titlelist)):
    sheet.write(0,i,titlelist[i])

# 保存工作簿
wb.save(r'data/students.xls')

