from lxml import etree
import requests
url =  'https://hz.lianjia.com/ershoufang/rs/'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
reponse = requests.get(url=url,headers=headers)
html_str = reponse.text if reponse.status_code == 200 else ''
root = etree.HTML(html_str)
# print(root)
# 导航、提取数据
# 1. 根据查看网页源代码、先提取包含了二手房的li标签
# //*[@id="content"]/div[1]/ul
li_list = root.xpath(r'./body/div[@class="content "]/div[@class="leftContent"]/ul/li')
# print(li_list,len(li_list))
# 2. 提取每个二手房信息
for i in li_list:
    house_title = i.xpath(r'./div[1]/div[1]/a/text()')[0]
    house_price = i.xpath(r'./div[1]/div[last()]/div[1]/span/text()')[0] +\
                  i.xpath(r'./div[1]/div[last()]/div[1]/i[2]/text()')[0]
    house_average_price = i.xpath(r'./div[1]/div[last()]/div[2]/span/text()')[0]
    print(house_title,house_price,house_average_price)