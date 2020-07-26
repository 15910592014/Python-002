# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MjspidersPipeline:
# 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        film_name = item['电影名称']
        film_type = item['电影类型']
        film_time = item['上映时间']
        output = f'|{film_name}|\t|{film_type}|\t|{film_time}|\n\n'
        with open('./maoyan.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item