import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 按照分类统计数量

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)
df = pd.read_excel(r'E:\python\Code\analysis_final\DouBanMovie\DouBanMovie\douBan_details.xlsx')


# DataFrame 选取其中的两列数据
filmType = df[['name', 'film_type']]
# 将film_type中的数据按','进行划分,按最多的划分次数,
df.film_type = filmType.film_type.str.split(pat=',', n=-1, expand=False)
# print(filmType.film_type)
# 将每一个电影的多个类型拆分为每一列只对应一个类型，每个电影拆分为多列
newValues = np.dstack((np.repeat(df.name.values, list(map(len, df.film_type.values))),
                       np.concatenate(df.film_type.values)))
# print(newValues[0])

# 将二维的数据转为df
filmType = pd.DataFrame(data=newValues[0], columns=filmType.columns)
# print(filmType)

# 按电影类型分组
df2 = filmType.groupby('film_type').size()
# ax返回轴
ax = df2.plot.bar()

# 通过.patch获得条形图的矩形
for rect in ax.patches:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height,
             str(height), size=10, ha='center', va='bottom')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
