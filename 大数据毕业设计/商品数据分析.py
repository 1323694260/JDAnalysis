import pandas as pd
from pyecharts.charts import pie
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)

plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_csv('商品信息.csv', encoding='gbk')
# 去掉米家后面的（MIJIA）
data['品牌'] = data['品牌'].str.replace('（MIJIA）', '')
# 取出评论数前十的产品
name_comment = data[['标题', '总评数']].groupby('标题', as_index=False).mean().sort_values(by=['总评数'], ascending=False)[:10]
# 按评论数排行的进入TOP10的品牌产品数量
brand_num_top10 = data[data['标题'].isin(name_comment['标题'])][['品牌', '总评数']].groupby('品牌',
                                                                                   as_index=False).count().sort_values(
    by=['总评数'], ascending=False)
print(name_comment['标题'])

brand_comment = data[['品牌', '总评数']].groupby('品牌', as_index=False).sum().sort_values(by=['总评数'], ascending=False)[:10]
print(brand_comment)

plt.pie(brand_num_top10['总评数'], labels=brand_num_top10['品牌'], autopct='%1.1f%%', shadow=False, startangle=150)
plt.show()
p = pie.Pie()
p.add("销量TOP10型号按品牌分布", brand_num_top10['品牌'], brand_num_top10['总评数'],
      is_label_show=True)
p.render('销量TOP10型号按品牌分布.html')
