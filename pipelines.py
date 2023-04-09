# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import numpy as np


class DoubanmoviePipeline:
    # 初始化操作
    def open_spider(self, spider):
        self.item_list = ["name", "number_evaluate", "score", "upTime", "area", "languages", "times", "film_type",
                          "star1", "star2", "star3", "star4", "star5"]
        # 导出excel
        self.f_excel = pd.ExcelWriter("douBan_details.xlsx")
        self.data_excel = []

    def process_item(self, item, spider):
        # 导出excel
        li_temp = np.array(list(dict(item).values()))
        li_data = []
        for i in range(len(li_temp)):
            li_data.append(str(li_temp[i]).replace("[", "").replace("]", "").strip('"').strip("'").replace("', '", ","))
        self.data_excel.append(li_data)

        return item

    def close_spider(self, spider):
        # 导出excel
        self.data_df = pd.DataFrame(self.data_excel)
        self.data_df.columns = self.item_list
        self.data_df.index = np.arange(1, len(self.data_df) + 1)
        self.data_df.to_excel(self.f_excel, float_format='%.5f')
        self.f_excel.save()

