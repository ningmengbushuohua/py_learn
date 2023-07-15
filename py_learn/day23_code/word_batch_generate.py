# 批量生成word: 离职证明
from docx import Document
person_list = [
    {
        "name":"杨天偿",
        "id":"333222199909120987",
        "sdate":"2017年7月1日",
        "edate":"2021年11月1日",
        "department":"技术部",
        "position":"架构师",
        "company":"深圳华为技术有限公司"
    },
    {
        "name":"刘一奇",
        "id":"110120198909120937",
        "sdate":"2016年3月1日",
        "edate":"2020年10月1日",
        "department":"行政部",
        "position":"打手",
        "company":"黑龙江天上人间桑拿会所"
    },
    {
        "name":"张国涛",
        "id":"111222199908120987",
        "sdate":"2015年4月1日",
        "edate":"2019年11月1日",
        "department":"后厨部",
        "position":"试吃员",
        "company":"深圳市金威源餐饮有限公司"
    },
    {
        "name":"欧阳",
        "id":"112221199909120987",
        "sdate":"2016年7月1日",
        "edate":"2020年11月1日",
        "department":"后勤部",
        "position":"大茶壶",
        "company":"深圳市怡红院高级会所"
    },
    {
        "name": "杨洋",
        "id": "112221199909120987",
        "sdate": "2016年7月1日",
        "edate": "2020年11月1日",
        "department": "后勤部",
        "position": "前台",
        "company": "深圳市国际监狱"
    },
    {
        "name": "蔡徐坤",
        "id": "112221199909120987",
        "sdate": "2016年7月1日",
        "edate": "2020年11月1日",
        "department": "头牌",
        "position": "头牌",
        "company": "bilibili鬼畜区"
    },
]

# 遍历列表，批量生成离职证明
for person in person_list:
    # 1.读取离职证明的模板文件
    doc = Document(r'data/离职证明模板.docx')

    # 2.数据处理
    for p in doc.paragraphs:
        # 过滤无需处理的段落
        if "{" not in p.text:
            continue
        # print(p.text)
        # 处理带有{的段落
        for run in p.runs:
            # 过滤无需处理的run 对象
            if "{" not in run.text:
                continue
            print(run.text)     # {name}
            # 将模板中形如  {xxx} 的数据替换掉
            # 通过切片，获取数据 xxx ,就可以匹配字典中的key
            key = run.text[1:-1]
            print(key)      # name
            print(person[key])
            # 替换        *****
            run.text = run.text.replace(run.text, person[key])


    # 3.将处理之后的数据进行保存
    doc.save(f'data/{person["name"]}的离职证明.docx')


# 说明： 如果需要批量生成文件，则需要提前准备模板 【一定要考虑到段落的组成】，就可以借助上述代码的思想操作
