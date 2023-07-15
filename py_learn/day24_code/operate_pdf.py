# 读取pdf以及加密pdf 文件
import PyPDF2
'''
PyPDF2.errors.DeprecationError: 废弃
PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.
PdfFileReader 已经被废弃   使用PdfReader替换
'''
# 2.0.0
# # 1.读取pdf中的文本内容
# reader = PyPDF2.PdfFileReader(r'data/XGBoost.pdf')
# # a.获取pdf指定页，返回一个字典
# page = reader.getPage(0)
# print(page)
# # b.获取指定页的文本内容
# text = page.extractText()
# print(text)

# 3.0.0
# 1.读取pdf中的文本内容
# reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
# # a.获取pdf指定页，返回一个字典
# page = reader.pages[0]
# print(page)
# # b.获取指定页的文本内容
# text = page.extract_text()
# print(text)

# 2.加密pdf文件
 # 创建读取文件的对象
reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
# 创建写入文件的对象
writer = PyPDF2.PdfWriter()

# 获取已知文件的每一页，添加到新的文件对象中

for i  in range(len(reader.pages)):
    writer.add_page(reader.pages[i])

# 给pdf加密
writer.encrypt('zhangliang')        # *****
with open(r'data/XGBoost-加密.pdf', 'wb') as f:
    writer.write(f)
