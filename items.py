# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    name = scrapy.Field()
    release_data = scrapy.Field()
    area = scrapy.Field()
    languages = scrapy.Field()
    times = scrapy.Field()
    film_type = scrapy.Field()
    number_evaluate = scrapy.Field()
    score = scrapy.Field()
    star1 = scrapy.Field()
    star2 = scrapy.Field()
    star3 = scrapy.Field()
    star4 = scrapy.Field()
    star5 = scrapy.Field()
    pass
