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

# 问题一： 使用相对路径staffs 节点下的三个name 节点,结果是列表
name_list = root.xpath(r'./staffs/name')
print(name_list)

# 问题二： 获取所有的name节点
name_list1 = root.xpath(r'//name')
print(name_list1,len(name_list1))

# 问题三：获取三个员工的名字和年龄
# 在路径表达式最后，
# 添加/text()，可以得到节点中的文本节点
# 添加/@属性，可以得到其对应的属性值

name = root.xpath(r'./staffs/name/text()')
print(name)
age = root.xpath(r'./staffs/name/@age')
print(age)

# 谓语，在路径中需要添加条件的节点后面添加[]，在[] 中写条件
# 1.[N]:表示获取第N个节点，从数字1开始

# 获取第二个员工姓名
print(root.xpath(r'./staffs/name[2]/text()'))
# 获取倒数第二个员工姓名------> [last()]:倒数第一个
print(root.xpath(r'./staffs/name[last()-1]/text()'))

# 2.position():获取某些位置的标签
# 获取前两个员工的年龄
print(root.xpath(r'./staffs/name[position()<=2]/@age'))
print(root.xpath(r'./staffs/name[position()<3]/@age'))

# 获取后两个员工的姓名
print(root.xpath(r'./staffs/name[position()>1]/text()'))
print(root.xpath(r'./staffs/name[position()>=2]/text()'))
print(root.xpath(r'./staffs/name[position()>=last()-1]/text()'))

# 3.[@属性名]
# 获取有sex属性的员工姓名
print(root.xpath(r'./staffs/name[@sex]/text()'))

# 4.[@属性名=属性值]
#   获取属性名gender ='女'的员工的年龄
print(root.xpath(r'./staffs/name[@gender="女"]/@age'))
print(root.xpath(r"./staffs/name[@gender='女']/@age"))

# 分支： |
# 将多个路径表达式用| 间隔，同时获取多个元素
print(root.xpath('./staffs/name/text()|./staffs/name/@sex|./staffs/name/@gender'))

# 总结：与CSS选择器一样，xpath 路径表达式同样需要灵活搭配组合

# 获取后三个商品的名字和价格
print(root.xpath(r'./goods/name[position()>=last()-2]/text()'))
print(root.xpath(r'./goods/name[position()>=last()-2]/@price'))
