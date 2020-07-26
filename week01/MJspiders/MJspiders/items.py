# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MjspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 注释原有的pass
    # pass
    film_name = scrapy.Field()
    film_type = scrapy.Field()
    film_time = scrapy.Field()