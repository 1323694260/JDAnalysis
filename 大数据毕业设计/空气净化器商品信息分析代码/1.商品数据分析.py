import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)


data = pd.read_csv(u'商品信息.csv', engine='python')
# 去掉米家后面的（MIJIA）
data['品牌'] = data['品牌'].str.replace('（MIJIA）', '')
# print(data)
# 取出评论数前十的产品
name_comment = data[['标题', '总评数']].groupby('标题', as_index=False).mean().sort_values(by=['总评数'], ascending=False)[:10]
print(name_comment)
# 按评论数排行的进入TOP10的品牌产品数量
brand_num_top10 = data[data['标题'].isin(name_comment['标题'])]
brand_num_top10[['品牌', '总评数']].groupby(by='品牌', as_index=False).count().sort_values(by=['总评数'], ascending=False)
# print(brand_num_top10)
#/
brand_comment = data[['品牌', '总评数']].groupby('品牌', as_index=False).sum().sort_values(by=['总评数'], ascending=False)[:10]
# print(brand_comment)

plt.pie(brand_num_top10['总评数'], labels=brand_num_top10['品牌'], autopct='%1.1f%%', shadow=False, startangle=150)
plt.show()
# pie = p.Pie()
# pie.page_title="销量TOP10型号按品牌分布"
# pie.add(brand_comment['名称'], brand_comment['总评数'].astype('float'))
# pie.render('1.pie.html')

