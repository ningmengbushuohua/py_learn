from bs4 import BeautifulSoup
import csv
import requests
from tqdm import tqdm
# 1.中国新闻网翻页
# https://www.chinanews.com/scroll-news/news3.html
# https://www.chinanews.com/scroll-news/news4.html
# https://www.chinanews.com/scroll-news/news10.html

# 数据持久化
# 1.创建文件，并打开
with open(r'data/中国新闻网.csv',mode='w',encoding='utf-8',newline='') as f:
    # newline='' ---> 如皋不写，Windows 系统下csv文件每一行数据后面会有一个空行
    # 翻页操作
    # 2.写列名
    col_name =['新闻类型','新闻标题','新闻链接','新闻时间']
    csv.writer(f).writerow(col_name)

    # --------------------------
    # 翻页操作
    for page in tqdm(range(1,11)):
        # print(f'第{page}开始爬取')
        url = f'https://www.chinanews.com/scroll-news/news{page}.html'
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        reponse = requests.get(url=url, headers=headers)
        if reponse.status_code != 200:
            print(f'爬取失败,状态码{reponse.status_code}')
        else:
            reponse.encoding = 'utf-8'
            # print(reponse.text)
        soup = BeautifulSoup(reponse.text, 'html.parser')
        # 从文档树中提取信息

        # 提取所需要的li标签
        li_list = soup.select('html > body > div.w1280.mt20 > div.content-left ul > li')
        # print(li_list)
        #  单独提取每一条新闻
        for i in li_list:
            # 分步骤写，讲究头尾呼应！！
            # 新闻类型
            if i.select_one('li > div.dd_lm > a') != None:
                news_type = i.select_one('li > div.dd_lm > a').text
                # 新闻标题
                news_title = i.select_one('li > div:nth-of-type(2) > a').text

                # 新闻链接
                news_href = 'https://www.chinanews.com' + i.select_one('li > div:nth-of-type(2) > a').attrs['href']

                # 发布时间
                news_time = i.select_one('li > div.dd_time').text
                # print(news_type, news_title, news_href, news_time)

                # 3.写入新闻
                # writerow :单行写入
                # writerows:多行写入
                news_data = [news_type, news_title, news_href, news_time]
                csv.writer(f).writerow(news_data)

                # 4. 关闭
                # print('数据存储完毕，文件保存关闭')

# 2. 豆瓣电影top250
# 第一页：https://movie.douban.com/top250?start=0&filter=
# 第二页：https://movie.douban.com/top250?start=25&filter=
# 第六页：https://movie.douban.com/top250?start=125&filter=
# 第十页：https://movie.douban.com/top250?start=225&filter=
for page in range(10):
    url1 = f'https://movie.douban.com/top250?start={page * 25}&filter='
    print(url1)
