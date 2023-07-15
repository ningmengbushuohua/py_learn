import PyPDF2

# 旋转和创建空白的pdf

# 1.旋转
 # 创建读取文件的对象
reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
# 创建写入文件的对象
writer = PyPDF2.PdfWriter()

for i in range(len(reader.pages)):
    # 获取每一页对象
    page = reader.pages[i]
    if i % 2 == 0:
        # 顺时针旋转90
        page.rotate(90)
    else:
        # 逆时针旋转
        page.rotate(-90)
    writer.add_page(page)


# 2.创建空白页
blank_page = writer.add_blank_page()

with open(r'data/XGBoost-旋转.pdf','wb') as f:
    writer.write(f)