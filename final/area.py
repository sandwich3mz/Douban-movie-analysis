import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 按照出品地区统计数量

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)
df = pd.read_excel(r'E:\python\Code\analysis_final\DouBanMovie\DouBanMovie\douBan_details.xlsx')

# DataFrame 选取其中的两列数据
area = df[['name', 'area']]
# 清除df中所有的空格
area.replace('\s+','', regex=True, inplace=True)
# 将area中的数据按'/'进行划分,按最多的划分次数,
df.area = area.area.str.split(pat='/', n=-1, expand=False)
# print(df.area)
# 将每一个电影的多个地区拆分为每一列只对应一个地区，每个电影拆分为多列
newValues = np.dstack((np.repeat(df.name.values, list(map(len, df.area.values))),
                       np.concatenate(df.area.values)))
# print(newValues[0])
# 将二维的数据转为df
area = pd.DataFrame(data=newValues[0], columns=['movie', 'area'])
# print(area)
# 将数据按地区分类并获得频次
df2 = area.groupby('area').size()
# 频次为1的国家计数器
ans = 0
# 频次为1的国家列表
arr = []
# 统计频次为1的国家
for i, v in df2.items():
    if v == 1:
        arr.append(i)
        ans = ans + 1
# print(arr)
# print(ans)
# 从df中清除频次为1的国家
df2.drop(arr, axis=0, inplace=True)
# print(df2)
# 将频次为1的国家统一为其他分类插入到df中
df2['其他'] = ans
# print(df2)
# ax返回轴
ax = df2.plot.bar()
# 通过.patch获得条形图的矩形
for rect in ax.patches:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), size=10, ha='center', va='bottom')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()

