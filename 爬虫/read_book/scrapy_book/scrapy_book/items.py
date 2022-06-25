# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


 # 网页数据结构
class ScrapyDocumentItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    create_time = scrapy.Field()
    summary = scrapy.Field()
    pic = scrapy.Field()
    url = scrapy.Field()
    site = scrapy.Field()


# 链接关系
class ScrapyLinkItem(scrapy.Item):
    parent_url = scrapy.Field()
    childer_url = scrapy.Field()