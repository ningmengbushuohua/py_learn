# api 接口数据的抓取
# 1. api 接口 简介
'''
API接口是负责传递数据的，在现今已存在的网站中，
除了极个别非常古老的网站，大部分的网站都会采用
API进行数据的传输。那么为什么API接口这么受欢迎呢，
那当然是其带来了很多的好处，最直观的便是节省了
开发的大量时间、大量金钱。举个例子：一个编程团队
想制作一个游戏，在这个游戏里有付费的功能，那么就
需要有一个支付的平台，而众所周知，支付平台是需要
有很大能力去保证安全且需要一定的资金还有资质的，
普通的团队压根搞不起啊，所以，这个团队，就需要用
到“API接口”，他可以接入其他的支付平台API接口实现
支付功能，这样就省去了很多的麻烦。所以，不例外的
我们要获取的数据也是可以通过API接口传递到页面中的，
那么如何利用好API接口，这便是我们要学习的了。
'''
# 2.api 接口的构造
# api 接口由请求地址和请求参数构成，请求地址和请求参数使用？连接，
# 请求参数 写成key=value的形式（键值对形式），如果有多个请求参数，使用&连接

'''
https://v.api.aa1.cn/api/api-qq-gj/index.php?qq=78238&num=68&vip=1
请求地址，顾名思义就是你请求的服务器的入口；
请求参数，就是按照设定你得告诉服务器你要做什么。
尝试打开这个链接了，结果发现什么也没有，那是因为这个API的请求参数设定不正确。
'''

# 3. api接口的请求
import requests
api_url = 'https://v.api.aa1.cn/api/api-qq-gj/index.php?qq=78238&num=68&vip=1'
reponse = requests.get(url=api_url)
result = reponse.text if reponse.status_code == 200 else reponse.status_code
print(result, type(result))
