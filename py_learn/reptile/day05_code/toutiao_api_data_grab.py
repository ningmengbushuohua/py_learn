# 今日头条api接口爬取及解析
import requests
import json
api_url = 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc&_signature=_02B4Z6wo00d01fo2QWwAAIDAcX3ajAT1qgX6EkXAABoi847w9mo6RPhGA0.9DlsnVHy.C.qF51KVvSv.5MmdikZ8Qd3h5rl-KiNvnTsOq5I3WJ9pwkX55YmS-qfG6wBV1x747h9SZOPWgAlI15'
reponse = requests.get(url=api_url)
result = reponse.text if reponse.status_code == 200 else reponse.status_code
# print(result)

# 绝大部分网站都有API接口，但是不一定能找到。
# 如果找不到就必须使用一些强制手段，例如：js逆向、使用抓包工具等。

news_data = json.loads(result)
print(news_data, type(news_data))

# 新闻提取
for i in news_data['data']:
    news_title = i['Title']
    news_href = i['Url']
    print(news_title, news_href)
