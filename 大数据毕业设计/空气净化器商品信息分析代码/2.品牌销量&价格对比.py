#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Bar,Overlap,Line

plt.rcParams['font.sans-serif'] = ['SimHei']
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

data = pd.read_csv(u'商品信息.csv',engine='python')
#统一品牌名
data['品牌'] = data['品牌'].str.replace('（MI）''|''（MIJIA）''|''（PHILIPS）''|''（Honeywell）''|''（Blueair）''|''（Panasonic）', ' ').dropna()
data['品牌']= data['品牌'].str.replace('米家','小米').str.strip()
#品牌总销量/品牌总价格
name_comment = data[['品牌','总评数','价格']].groupby('品牌',as_index=False).sum().sort_index(by=['总评数'],ascending=False)[:5]
#总数量
number_price = data[['品牌','总评数','价格']].groupby('品牌',as_index=False).count().sort_index(by=['总评数'],ascending=False)[:5]
# print('-----------')
name = name_comment['品牌']
print(list(name))
General_comments = list(name_comment['总评数'])
print('总评论：',General_comments)
total_price  = list(name_comment['价格'])
print('总价格',total_price)
total_number = list(number_price['价格'])
print('总数量',total_number)

#总价格/总数量=平均价格
mean_price = []
[mean_price.append(comment[0]/comment[1]) for comment in zip(total_price,total_number)]
print('平均价格',mean_price)

# l=[i for i in range(5)]
#
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
#
# ax1.plot(l,mean_price,'or-',color='red',label=u'平均价格')
#
# for i,(_x,_y) in enumerate(zip(l,mean_price)):
#     plt.text(_x,_y,mean_price[i],color='black',fontsize=10)  #将数值显示在图形
#
# ax1.legend(loc=1)
# ax1.set_ylim([0,5000])
# ax1.set_ylabel(['mean_price'])
#
# ax2 = ax1.twinx()
# plt.bar(l,General_comments,alpha=0.3,label=u'品牌销量')
#
# for i,(_x,_y) in enumerate(zip(l,General_comments)):
#     plt.text(_x,_y,General_comments[i],color='green',fontsize=10)
#
# ax2.legend(loc=2)
# ax2.set_ylim([0, 2000000])  #设置y轴取值范围
#
# plt.xticks(l,name)
# plt.show()

bar = Bar(width=1200,height=600)
bar.add("品牌销量",name,General_comments, is_label_show=True)

line = Line()
line.add("平均价格",name,mean_price)

overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render("2品牌销量_价格对比.html")

