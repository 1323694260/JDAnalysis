import pandas as pd
from pyecharts import Bar

data = pd.read_csv('商品信息.csv', engine='python')
data['品牌'] = data['品牌'].str.replace('（MI）''|''（MIJIA）''|''（PHILIPS）''|''（Honeywell）''|''（Blueair）''|''（Panasonic）',
                                    ' ').dropna()
data['品牌'] = data['品牌'].str.replace('米家', '小米').str.strip()
name = ['小米', '飞利浦', '松下']
# 筛选出前3品牌所有信息
xiaomi_city = data[data['品牌'].isin(['小米'])]
feilipu_city = data[data['品牌'].isin(['飞利浦'])]
songxia_city = data[data['品牌'].isin(['松下'])]
# 前3品牌的价格
xiaomi_price = list(xiaomi_city['价格'])
feilipu_price = list(feilipu_city['价格'])
songxia_price = list(songxia_city['价格'])

xiaomi_0_1,feilipu_0_1,songxia_0_1= [],[],[]

xiaomi = [len([xiaomi_0_1.append(j) for j in xiaomi_price if i < j < i+1000]) for i in range(0,22000,1000)]
feilipu = [len([feilipu_0_1.append(i) for i in feilipu_price if k < i < k+1000]) for k in range(0,22000,1000)]
songxia = [len([songxia_0_1.append(i) for i in songxia_price if l < i < l+1000]) for l in range(0,22000,1000)]

x = ['%sk'%i for i in range(1,23)]

bar = Bar(width=1800, height=900)
bar.add("小米", x, xiaomi,is_label_show=True, line_color='blue')
bar.show_config()
bar.add("飞利浦", x, feilipu,is_label_show=True, line_color='green')
bar.show_config()
bar.add("松下", x, songxia,is_label_show=True)
bar.show_config()
bar.render('2.2商品价格区间.html')
