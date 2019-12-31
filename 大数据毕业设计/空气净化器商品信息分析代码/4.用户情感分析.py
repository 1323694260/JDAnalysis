# 好评率:好评人数/总评价人数
from itertools import chain

import pandas as pd
from pyecharts import Pie
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
# commodity_x ,good_comment,centre_comment,chase_comment,check_comment = [],[],[],[],[]
name_index = ['2S|2s','AC4076','F-PDF35C-G']
# for i in name_index:
good_comment1 = [sum(data[data['标题'].str.contains(i)]['总评数']) for i in name_index]
centre_comment1 = [sum(data[data['标题'].str.contains(i)]['好评数'])for i in name_index]
check_comment1 = [sum(data[data['标题'].str.contains(i)]['差评数'])for i in name_index]
chase_comment1 = [sum(data[data['标题'].str.contains(i)]['追评数'])for i in name_index]
good_comment = sum(data[data['标题'].str.contains(name_index[1])]['好评数'])
check_comment = sum(data[data['标题'].str.contains(name_index[1])]['差评数'])
itme = []
itme.append(good_comment)
itme.append(check_comment)
# 好评率:好评人数/总评价人数
# feedback1 = [centre_comment1[i]/good_comment1[i] for i in range(3)]
feedback1 = [((centre_comment1[i]-check_comment1[i])+chase_comment1[i])/good_comment1[i] for i in range(3)]
print('小米2S,飞利浦AC4076,松下F-PDF35C-G各综合得分：',feedback1)
#指定评价等级和评价标准
#先制定出各项评价指标，统一的评价等级，分值范围
#偏差率 = 100% * （投标人评标价-评标基准价）/评标基准价
# （好评-差评）*50 + 追评 *50 /总评论 = 综合得分
# 个商品综合得分 = 好评 *77.27% + 追评* 0.34% + 晒单*0.59%+ 差评*0.179%+中评+0.179% + 未评价（75,495）‬*21.26%#
print(itme)
print(itme[0]/sum(itme))
judge = ['正面','负面']
# pie = Pie('飞利浦AC4076', width=1200, height=600)
pie = Pie('松下F-PDF35C-G', width=1200, height=600)
# pie = Pie('小米2s空气净化器', width=1200, height=600)
# pie.add('小米2s空气净化器', judge, itme, radius=[25,50], is_label_show=True)
# pie.add('飞利浦AC4076', judge, itme, radius=[25,50], is_label_show=True)
pie.add('松下F-PDF35C-G', judge, itme, radius=[25,50], is_label_show=True)
pie.render('4.1用户情感分析松下F-PDF35C-G.html')


