# 使用爬虫 遇到封禁IP地址的反爬措施

# 1.代理ip 简介
# 代理ip 又叫代理服务器，其功能是代替网络用户去获取网络信息

# 2. 代理ip应用场景
# 防止我们的ip被封禁，可以使用代理ip等
# https://www.zmhttp.com/  芝麻代理

# 3. 代理ip的使用
# a. 从api接口提取IP
import requests
import json

api_url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
# 代理ip服务商不要求我们伪装爬虫
reponse = requests.get(url=api_url)
api_dict = json.loads(reponse.text)
print(api_dict)

# b. 构造代理ip
ip = api_dict['data'][0]['ip']
port = api_dict['data'][0]['port']
# 构造代理ip的字典的作用：市面上大部分ip走的协议为http协议，
# 但是当前很多网站已经是https协议，构造字典的作用是为了不管是http还是https的网站都使用http协议
proxy = {
    'http':f'http://{ip}:{port}',
    'https':f'http://{ip}:{port}'
}
print(proxy)

# c.使用代理ip 访问豆瓣网站
url = 'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
reponse = requests.get(url=url, headers=headers, proxies=proxy)
if reponse.status_code == 200:
    print('代理ip 使用成功')
    print(reponse.text)
