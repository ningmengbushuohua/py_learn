import re
import scrapy
from ..items import ChinaNewsItem
# 爬虫

class ChinaNewsSpiderSpider(scrapy.Spider):
    name = 'china_news_spider'
    allowed_domains = ['www.chinanews.com']
    start_urls = ['http://www.chinanews.com/']

    def parse(self, response):
        # print(response)
        href = response.css(
            'body > div.w1280 > div.news-right > div.top-jsxw > div:nth-child(1) > a::attr(href)').get()
        # get() 当做select_one 和text 的结合
        # print(href)
        # https://www.chinanews.com.cn/scroll-news/news1.html
        # /scroll-news/news1.html
        for page in range(1,11):
            link = self.start_urls[0] + re.sub(r'\d', str(page), href[1:])
            # print(link)
            # 链接 构造生成器，针对这十个链接进行请求，通过回调函数NewsInfo() 方法对请求结果处理
            yield scrapy.Request(url=link, callback=self.NewsInfo)
            # callback: 回调函数

    def NewsInfo(self, reponse):
        # 注意此时的最后一个li 应该是去掉nth-child
        # body > div.w1280.mt20 > div.content-left > div.content_list > ul > li:nth-child(2)
        li_list = reponse.css('body > div.w1280.mt20 > div.content-left > div.content_list > ul > li')
        for i in li_list:
            if i.css('li::attr(class)').get() != 'nocontent':
                # 新闻类型
                news_type = i.css('li > div.dd_lm > a::text').get()
                # 新闻标题
                news_title = i.css('li > div.dd_bt > a::text').get()
                # 新闻链接
                news_link = self.start_urls[0][:-1] + i.css('li > div.dd_bt > a::attr(href)').get()
                # https://www.chinanews.com.cn/sh/2023/07-14/10043241.shtml
                # 新闻时间
                news_time = i.css('li > div.dd_time::text').get()
                # print(news_type, news_title, news_link, news_time)
                # 每一页的内容已得到

                news_item = ChinaNewsItem()
                news_item['news_type'] = news_type
                news_item['news_title'] = news_title
                news_item['news_link'] = news_link
                news_item['news_time'] = news_time
                # 生成器
                yield news_item
