# lxml 解析数据
from lxml import etree

with open(r'xml_case.xml','r',encoding='utf-8') as f:
    result = f.read()
# print(result)

# 使用etree 中的XML 方法和HTML 方法分别对xml 文档和html 文档进行解析
# 返回一个_Element对象（树结构），使用XPath 路径表达式进行导航，查找提取信息
root = etree.XML(result)
print(root)
# 针对 _Element 对象使用xpath方法导航提取数据
# 语法：_Element 对象.xpath('路径表达式')
# 路径表达式分为绝对路径和相对路径（主要使用）
# 相对路径： 哪个节点对象在调用xpath方法，这个节点就写为(.)点，然后从此处一层一层开始写
# 注意：节点和节点之间使用 / 间隔，直接跨越节点要使用 //

# 问题一： 使用相对路径staffs 节点下的三个name 节点
