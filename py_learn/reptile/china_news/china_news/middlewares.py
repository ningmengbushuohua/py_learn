# Define here the models for your spider middleware
# 中间件
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 爬虫中间件
class ChinaNewsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod    # 类方法
    def from_crawler(cls, crawler):
        # 爬虫执行前 初始化
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 爬虫异常
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 下载中间件
class ChinaNewsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# user-agent 中间件
class UserAgentDownloadMiddleware:
    '''
    在下载中间件中添加UserAgent 反反爬
    '''
    def __init__(self):
        # 初始化方法
        with open('UserAgent.txt','r',encoding='utf-8') as f:
            # f.read() 读出的结果为字符串，需要将字符串转为原本的类型：列表。
            # eval() ： 能够将字符串、整型、浮点型、布尔、列表等转换为其原本的类型
            read_result = f.read()
        self.user_agent_list = eval(read_result)

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        # 爬虫出现异常时
        pass

    def spider_opened(self, spider):
        # 爬虫开始时
        spider.logger.info('Spider opened: %s' % spider.name)

# 代理ip 中间件
class ProxyIpDownLoaderMiddleware:
    pass