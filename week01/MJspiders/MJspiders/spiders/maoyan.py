# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from MJspiders.items import MjspidersItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        items = []
        # soup = BeautifulSoup(response.text, 'html.parser')
        item = MjspidersItem()

        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            film_name = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]')
            film_type = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]')
            film_time = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]')
            item["电影名称"] = film_name
            item["电影类型"] = film_type
            item["上映时间"] = film_time
            items.append(item)
        yield item 


