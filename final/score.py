import pandas as pd
from matplotlib import pyplot as plt
# 获得星级分布图，以便分析每部电影的1-5星分布


def percentage(begin1, begin2):
    # 读取数据
    df = pd.read_excel(r'E:\python\Code\analysis_final\DouBanMovie\DouBanMovie\douBan_details.xlsx')
    # 将每个星级字符型的百分比转为小鼠与电影分数相乘求出由该星级打分所获得的分数
    df["star1"] = df['star1'].str.strip("%").astype(float) / 100
    df["star1_value"] = df["star1"].values * df["score"].values

    df["star2"] = df['star2'].str.strip("%").astype(float) / 100
    df["star2_value"] = df["star2"].values * df["score"].values

    df["star3"] = df['star3'].str.strip("%").astype(float) / 100
    df["star3_value"] = df["star3"].values * df["score"].values

    df["star4"] = df['star4'].str.strip("%").astype(float) / 100
    df["star4_value"] = df["star4"].values * df["score"].values

    df["star5"] = df['star5'].str.strip("%").astype(float) / 100
    df["star5_value"] = df["star5"].values * df["score"].values

    # 将获得的起始点转为int型方便计算
    begin1 = int(begin1)
    begin2 = int(begin2)

    # 结束点为起始点加5
    tail1 = begin1 + 5
    tail2 = begin2 + 5

    # 截取数据
    df1 = df[begin1:tail1]
    df2 = df[begin2:tail2]

    # 拼接数据
    df_fn = pd.concat([df1, df2])

    # 绘制叠加柱形图
    df_fn.plot.bar(x='name', y=['star1', 'star2', 'star3', 'star4', 'star5'], stacked=True,
                   color=['#002c53', '#ffa510', '#0c84c6', '#ffbd66', '#f74d4d'])
    # 设置标题
    plt.xlabel('电影')
    plt.ylabel('评分')
    plt.title("星级分布图")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 设置图例位置
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    # 为了使对照更加明显,让用户选择两个起始点，每个起始点开始显示5条数据
    head1 = input("将为您显示5条电影信息的星级分布,请输入0-245中的一个数作为起始点1:")
    head2 = input("将为您显示5条电影信息的星级分布,请输入0-245中的一个数作为起始点2:")
    percentage(head1, head2)
