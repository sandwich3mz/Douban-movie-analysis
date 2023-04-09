import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 获取Top250电影月份分布图

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 1000)
# 显示完整的行
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 1000)
df = pd.read_excel(r'E:\python\Code\analysis_final\DouBanMovie\DouBanMovie\douBan_details.xlsx')

# DataFrame 选取其中的两列数据
time = df[['name', 'upTime']]
# 清除df中所有的空格
time.replace('\s+','', regex=True, inplace=True)
# 将time中的数据按','进行划分,按最多的划分次数,
df.time = time.upTime.str.split(pat=',', n=-1, expand=False)
# print(df.time)
# 将每一个电影的多个上映时间拆分为每一列只对应一个时间，每个电影拆分为多列
newValues = np.dstack((np.repeat(df.name.values, list(map(len, df.time.values))),
                       np.concatenate(df.time.values)))
# print(newValues[0])

# 将二维的数据转为df
time = pd.DataFrame(data=newValues[0], columns=['movie', 'time'])

# 将时间进行分为年月日地点 expand=True表示转化为dataFrame
time_temp = time['time'].str.split('[-()/]', expand=True)

# 连接两个dataFrame对象
time = pd.concat([time, time_temp], axis=1)

# 删除原来的时间列和列标为4的空白列
time = time.drop(columns=[4, 'time'], inplace=False, axis=1)

# 将列标重命名
time.rename(columns={0: 'year', 1: 'month', 2: 'day', 3: 'area'}, inplace=True)
time.groupby(['month']).size().plot(kind='pie', y=1, autopct='%1.0f%%')
plt.title("Top250电影月份分布图")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()

