# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # 车型
    car = scrapy.Field()
    # 购买时间
    time = scrapy.Field()
    # 公里数
    road = scrapy.Field()
    # 报价
    price = scrapy.Field()
    # 爬虫名
    source = scrapy.Field()
