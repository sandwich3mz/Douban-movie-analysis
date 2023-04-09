import numpy as np
import pandas as pd
# 每个国家或地区排名前三的电影

# 显示完整的列
pd.set_option('display.max_columns', None)
# 显示完整的行
pd.set_option('display.max_rows', None)
# 设置不折叠数据
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 100)
df = pd.read_excel(r'E:\python\Code\analysis_final\DouBanMovie\DouBanMovie\douBan_details.xlsx')

# DataFrame 选取其中的三列数据
area = df[['name', 'score', 'area']]

# 清除df中所有的空格
area.replace('\s+','', regex=True, inplace=True)

# 将area中的数据按','进行划分,按最多的划分次数,
df.area = area.area.str.split(pat='/', n=-1, expand=False)
# print(df.area)

# 将电影名称和电影评分数组合并在一起
name_and_score = np.array([df.name.values, df.score.values])
# 将电影名字和电影评分根据地区个数重复
name_and_score1 = np.repeat(name_and_score, list(map(len, df.area.values)), axis=1)
# 将二维数组转化成一维数组
areaArr = np.concatenate(df.area.values)
# print(areaArr)
# 将电影名称、电影评分、所属地区合成为数组
newValues = np.dstack((name_and_score1[0], name_and_score1[1], areaArr))
# print(newValues)

# 将二维的数据转为df
area = pd.DataFrame(data=newValues[0], columns=['movie', 'score', 'area'])
# print(area)

rank = area.sort_values('score', ascending=False)

# 将数据按地区分类
print(rank.groupby('area', group_keys=True).apply(lambda x: x.head(3)[:]).drop(axis=1, columns='area', inplace=False))
