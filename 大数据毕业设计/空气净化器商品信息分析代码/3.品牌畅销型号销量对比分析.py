# 3、品牌畅销型号销量对比分析
#销量前3的品牌中找出两款畅销产品
#畅销=销量=商家个数=好评数量=回头客= #
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
commodity_x = []
sales_y = []
# 筛选出前3品牌所有信息 ['总评数','好评数','追评数','差评数']
[commodity_x.append(list(data[data['品牌'].isin([name[i]])]['名称'][:2]))for i in range(3)]
[sales_y.append(list(data[data['品牌'].isin([name[j]])]['总评数'][:2]))for j in range(3)]
x = list(chain(*commodity_x))
sales = list(chain(*sales_y))
name_index = ['2S|2s','pro','AC4076','AC4076/18','F-PDF35C-G','F-PXF35C-S']
#二维“标题”列找 name_index匹配的值，计数
merchant = [data[data['标题'].str.contains(h)]['标题'].count() for h in name_index]
bar = Bar(width=1200,height=600)
bar.add('畅销型号销量',x,sales,line_color='green', xaxis_rotate=30)
line = Line()
line.add("商家个数（出售此款产品）",x,merchant)
overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render('3.品牌畅销型号销量对比分析.html')


