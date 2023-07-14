# 使用爬虫频繁访问豆瓣
import requests


URL = 'https://movie.douban.com/top250?start=0&filter='
Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
while True:
    resp = requests.get(url=URL, headers=Headers)
    if resp.status_code == 200:
        print(resp.status_code)
    else:
        print(resp.status_code)
        break
