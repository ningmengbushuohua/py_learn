# 正则在爬虫中的运用
import requests,re

url = 'https://www.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
reponse = requests.get(url=url,headers=headers)


if reponse.status_code == 200:
    print('请求成功')
    # print(reponse.text)
    # + : 匹配一个或者多个 ？： 代表停下来，非贪婪
    regexp_str = '<span class="title-content-title">(.+?)</span>'
    r = re.findall(regexp_str, reponse.text)
    print(r)
else:
    print(f'请求失败：{reponse.status_code}')
