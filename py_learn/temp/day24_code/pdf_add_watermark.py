# pdf 添加水印
import PyPDF2

# 创建读取文件的对象
src_writer = PyPDF2.PdfReader(r'data/XGBoost.pdf')
water_reader = PyPDF2.PdfReader(r'data/watermark.pdf')

# 创建写入文件的对象
writer = PyPDF2.PdfWriter()

# 获取水印文件的page 对象
water_page = water_reader.pages[0]


# 遍历需要添加水印的pdf文件的每一页对象，将其和水印文件对象进行合并
for num in range(len(src_writer.pages)):
    src_page = src_writer.pages[num]
    # 合并
    src_page.merge_page(water_page)     # *********
    # 添加
    writer.add_page(src_page)

with open(r'data/XGBoost-水印.pdf','wb') as f:
    writer.write(f)
