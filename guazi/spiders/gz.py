# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from guazi.items import GuaziItem


class GzSpider(RedisCrawlSpider):
    name = 'gz'
    allowed_domains = ['guazi.com']
    # start_urls = ['https://www.guazi.com/xa/buy/o1/#bread']

    redis_key = "gzspider:start_urls"

    rules = (
        Rule(LinkExtractor(allow=r'/xa/buy/o\d+/#bread'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = GuaziItem()

        item['car'] = self.get_car(response)
        item['time'] = self.get_time(response)
        item['road'] = self.get_road(response)
        item['price'] = self.get_price(response)
        item['source'] = 'guazi'

        yield item

    def get_car(self, response):
        car = response.xpath("//h2[@class='t']/text()").extract()
        if len(car):
            pass
        else:
            car = "NULL"
        return car

    def get_time(self, response):
        time = response.xpath("//div[@class='t-i']/text()[1]").extract()
        if len(time):
            pass
        else:
            time = "NULL"
        return time

    def get_road(self, response):
        road = response.xpath("//div[@class='t-i']/text()[2]").extract()
        if len(road):
            pass
        else:
            road = "NULL"
        return road

    def get_price(self, response):
        price = response.xpath("//div[@class='t-price']/p/text()").extract()
        if len(price):
            pass
        else:
            price = "NULL"
        return price
