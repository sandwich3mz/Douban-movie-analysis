import scrapy
from scrapy import Request
from DouBanMovie.items import DoubanmovieItem
import time


class douBanSpider(scrapy.Spider):
    name = 'DouBanMovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ["https://movie.douban.com/top250"]
    step_time = 5
    page_number = 0

    def parse(self, response):
        node_list = response.xpath('//div[@class="info"]')

        for msg in node_list:
            # 详情链接
            details_url = msg.xpath('./div[@class="hd"]/a/@href').extract()
            # 中文名称
            name = msg.xpath('./div[@class="hd"]/a/span[1]/text()').extract()
            # 评论人数
            number_evaluate = msg.xpath('./div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()
            number_evaluate = str(number_evaluate)[2:-5]
            # 评分
            score = msg.xpath('./div[@class="bd"]/div[@class="star"]/span[@property="v:average"]/text()').extract()
            # 使用管道保存
            # 管道可以对键值自动去重
            item_pipe = DoubanmovieItem()
            item_pipe["name"] = name
            item_pipe["number_evaluate"] = number_evaluate
            item_pipe["score"] = score

            time.sleep(self.step_time)
            yield Request(details_url[0], callback=self.get_details, meta={"info": item_pipe})

        # 有序内容获取方法
        self.page_number += 1
        print(self.page_number)
        # 爬取其他页面
        if (self.page_number < 10):
            time.sleep(3)
            page_url = 'https://movie.douban.com/top250?start={}&filter='.format(self.page_number * 25)
            yield scrapy.Request(page_url, callback=self.parse)

    # 获取详情页数据
    def get_details(self, response):
        item_pipe = DoubanmovieItem()
        info = response.meta["info"]
        item_pipe.update(info)

        response = response.xpath('//div[@id="info"]')
        # 上映时间
        release_data = response.xpath('./span[@property="v:initialReleaseDate"]/text()').extract()
        # 制片国
        area = str(response.extract())
        area = area[area.index("制片国"):area.index("语言")].strip()
        area = area[area.index("</span>") + 7:area.index("<br>")].strip()
        # 语言
        languages = str(response.extract())
        languages = languages[languages.index("语言"):languages.index("上映")].strip()
        languages = languages[languages.index("</span>") + 7:languages.index("<br>")].strip()
        # 片长
        times = response.xpath('./span[@property="v:runtime"]/text()').extract()
        # 类型
        film_type = response.xpath('./span[@property="v:genre"]/text()').extract()

        # 1星占比
        star1 = response.xpath('//div[@class="item"][5]/span[@class="rating_per"]/text()').extract()
        # 2星占比
        star2 = response.xpath('//div[@class="item"][4]/span[@class="rating_per"]/text()').extract()
        # 3星占比
        star3 = response.xpath('//div[@class="item"][3]/span[@class="rating_per"]/text()').extract()
        # 4星占比
        star4 = response.xpath('//div[@class="item"][2]/span[@class="rating_per"]/text()').extract()
        # 5星占比
        star5 = response.xpath('//div[@class="item"][1]/span[@class="rating_per"]/text()').extract()

        item_pipe["release_data"] = release_data
        item_pipe["area"] = area
        item_pipe["languages"] = languages
        item_pipe["times"] = times
        item_pipe["film_type"] = film_type
        item_pipe["star1"] = star1
        item_pipe["star2"] = star2
        item_pipe["star3"] = star3
        item_pipe["star4"] = star4
        item_pipe["star5"] = star5

        yield item_pipe
