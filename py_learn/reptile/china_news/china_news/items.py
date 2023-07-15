# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 实体 构造数据，构造成字典
import scrapy


class ChinaNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Field() 接受数据
    news_type = scrapy.Field()
    news_title = scrapy.Field()
    news_link = scrapy.Field()
    news_time = scrapy.Field()
