# 中国新闻网爬取
import requests
from bs4 import BeautifulSoup

url = 'https://www.chinanews.com/scroll-news/news1.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
reponse = requests.get(url=url,headers=headers)
if reponse.status_code !=200:
    print(f'爬取失败,状态码{reponse.status_code}')
else:
    reponse.encoding= 'utf-8'
    # print(reponse.text)
soup = BeautifulSoup(reponse.text, 'html.parser')
# 从文档树中提取信息

# 提取所需要的li标签
li_list = soup.select('html > body > div.w1280.mt20 > div.content-left ul > li')
print(li_list)
#  单独提取每一条新闻
for  i in li_list:
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
        print(news_type, news_title, news_href, news_time)
