# requests 模块的安装
# pip install requests
import re
import requests
# requests模块：能够向网址发送请求（本质：向网站所在服务器发送请求），得到响应结果
url = 'https://www.baidu.com/'
# headers: 标头，作用：伪装爬虫的作用，使爬虫被伪装成浏览器。
# User-Agent：标头中的其中一个参数，它的存在足以应对大部分网站
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


# 向xxx网址发送请求，得到其给的响应结果（结果中包含了我们想要的结果）
reponse = requests.get(url=url, headers=headers)
print(reponse)
# 1. 状态码：状态码揭示了爬虫是否能用，status_code
# 200: 爬虫正常访问了服务器
# 403：爬虫被拒绝了
# 404：网页丢失
# 500： 服务器崩溃
print(reponse.status_code)

# 如果网页发生了乱码
# 如果网页发生了乱码，再写下方的一行代码： 其中utf-8代码网页的编码方式
# 网页源代码中一定规定了charset, 此时就可以将响应结果中的编码改掉
reponse.encoding = 'utf-8'

# 查看网页源代码： text,此时的网页源代码是字符串类型
# print(reponse.text)

# 使用正则表达式 从源代码中匹配信息

# 正则注意贪婪问题
# <span class="title-content-title">星辰大海里的中国名字</span>
regex_str = r'<span class="title-content-title">(.*?)</span>'
# 在findall 方法中，正则表达式的哪一部分有分组，最终获取的就是那一部分
result = re.findall(regex_str, reponse.text)
# print(result)
for i in result:
    print(i)
