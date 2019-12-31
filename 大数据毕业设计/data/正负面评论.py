import pandas as pd
from pyecharts.charts import line

def main(file, data):
    data['score'] = data['score'].astype('int')  # 转int
    data['reference_time'] = pd.to_datetime(data['reference_time'])  # 转时间
    data = data.sort_values(by='reference_time')  # 根据时间排序
    z = data[data['score'] > 4]    # 评分大于或等于4星为正面
    f = data[data['score'] <= 4]  # 评分小于4星为负面
    z_plot = z[['reference_time', 'score']].groupby(z['reference_time'].dt.date).count()
    f_plot = f[['reference_time', 'score']].groupby(f['reference_time'].dt.date).count()
    l = line.Line(width=1800, height=800)
    l.add("正面评论走势", z_plot.index, z_plot['score'])
    l.add("负面评论走势", f_plot.index, f_plot['score'])
    l.render(file+"用户正负面评论趋势.html")

if __name__ == '__main__':
    file = '小米2s评论.csv'
    # file = '飞利浦评论.csv'
    # file = '松下评论.csv'
    data = pd.read_csv(file, encoding='gbk')
    main(file, data)