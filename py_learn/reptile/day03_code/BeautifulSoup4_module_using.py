# 1. 简介
# BeautifulSoup 是一个用于从HTML 和XML文件中提取数据的python模块
# 使用BeautifulSoup模块，你可以提取到需要的任意信息
# BeautifulSoup4 是BeautifulSoup 系列模块的第四个大版本

# 2.安装
# Windows Linux mac
# python 可视化安装

# 3.解析数据
#  使用BeautifulSoup4 模块，前提是已经拿到了网页源代码（字符串）
html_str = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
'''
from bs4 import BeautifulSoup
# BeautifulSoup(网页源代码，解析器) ---> 使用BeautifulSoup 方法对网页源代码进行文档解析
# 返回一个BeautifulSoup对象（本质：树结构），这个解析过程需要使用解析器
soup = BeautifulSoup(html_str, 'html.parser')
#  对文档解析的过程，其实就是将HTML源代码转换为树结构，便于后续内容查找
print(soup, type(soup))

# 提取树结构中内容的方法和属性
'''
select() ： 使用CSS选择器（标签选择器，id选择器，class选择器，父子选择器，后代选择器、nth-of-type选择器等）
            从树结构中遍历符合css选择器的所有结果，存放在列表中
select_one()：使用CSS选择器（标签选择器，id选择器，class选择器，父子选择器，后代选择器、nth-of-type选择器等）
            从树结构中遍历符合css选择器的第一个结果
text(): 从标签内获取标签内容
attrs(): 从标签内，获取指定属性名对应的 属性值
'''

# Q1:提取p标签
# 标签选择器：只写标签名，会获取到整个HTML源代码中的所有某标签
p_list = soup.select('p')
print(p_list)

# 父子选择器：从最外层向最内层写，使用 > 连接（> 左右都要有空格）
p_list2 = soup.select('html > body > p')
print(p_list2)

# 后代选择器： 从外层写向内层，使用空格连接（空格右边是空格左边的后代）
p_list3 = soup.select('html p')
print(p_list3)

# Q2:获取三个拥有sister属性值得a 标签
# class选择器：使用.调用标签内的class属性值
a_list = soup.select('a.sister')
print(a_list)

# Q3:获取第二个a标签
# id选择器：使用# 调用标签内的id属性值
a = soup.select_one('a#link2')
print(a)

# Q4:获取第二个a的href属性值 和标签内容
a = soup.select_one('html > body a#link2')
print(a)
print(a.text, a.attrs['href'])

# nth-of-type(N):获取第N格某标签
a2 = soup.select_one('html > body a:nth-of-type(2)')
print(a2)
print(a2.text, a2.attrs['href'])

# 总结：标签选择器、id选择器等可以综合使用，这些选择器综合使用是为了使查找结果更准确