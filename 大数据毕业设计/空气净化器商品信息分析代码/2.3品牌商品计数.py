import pandas as pd
from pyecharts import Bar

data = pd.read_csv('商品信息.csv', engine='python')
data['品牌'] = data['品牌'].str.replace('（MI）''|''（MIJIA）''|''（PHILIPS）''|''（Honeywell）''|''（Blueair）''|''（Panasonic）', ' ').dropna()
data['品牌'] = data['品牌'].str.replace('米家', '小米').str.strip()
name = ['小米', '飞利浦', '松下']
#二维字段为“品牌”isin找几个品牌，并显示“品牌”和“价格”。分组根据“品牌”as_index设置索引，计数，排序，按“价格”，False降序 大-小
price_groupby = data[data['品牌'].isin(name)][['品牌', '价格']].groupby(by='品牌',as_index=False).count().sort_index(by='价格',ascending=False)
name = list(price_groupby['品牌'])
price = list(price_groupby['价格'])
# print(list(name))

bar = Bar(width=1200,height=600)
bar.add("品牌商品计数",name,price)
bar.show_config()
# bar.render()
bar.render("2_3品牌商品计数.html")