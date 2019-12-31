#畅销产品和平均价格
from itertools import chain

import pandas as pd
from pyecharts import Bar, Line, Overlap

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)
data = pd.read_csv('商品信息.csv', engine='python').dropna()
data['品牌'] = data['品牌'].str.replace('（MI）''|''（MIJIA）''|''（PHILIPS）''|''（Honeywell）''|''（Blueair）''|''（Panasonic）',
                                    ' ').dropna()
data['品牌'] = data['品牌'].str.replace('米家', '小米').str.strip()
name = ['小米', '飞利浦', '松下']
commodity_x ,sales_y,price_avg,price_y = [],[],[],[]
# 筛选出前3品牌所有信息
[commodity_x.append(list(data[data['品牌'].isin([name[i]])]['名称'][:2])) for i in range(3)]
[sales_y.append(list(data[data['品牌'].isin([name[j]])]['总评数'][:2]))for j in range(3)]
[price_y.append(data[data['品牌'].isin([name[j]])]['名称']) for j in range(3)]
x = list(chain(*commodity_x))
sales = list(chain(*sales_y))
name_index = ['2S','pro','AC4076','AC4076/18','F-PDF35C-G','F-PXF35C-S']
for h in name_index:
    merchant = data[data['标题'].str.contains(h)]['价格']
    price_avg.append(sum(merchant)/len(merchant))
bar = Bar(width=1200, height=600)   #is_label_show=True  每根柱子显示值
bar.add('畅销型号销量', x, sales, line_color='green',is_label_show=True,xaxis_rotate=30)
line = Line()
line.add( "平均价格",x, price_avg)
overlap = Overlap()
overlap.add(bar)
overlap.add(line, yaxis_index=1, is_add_yaxis=True)
overlap.render('3.2畅销产品和平均价格.html')


