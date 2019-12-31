import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
# 读取数据，给定字段名
data = pd.read_csv('FjData.csv',names=['城市', '小区名', '地址', '户型', '销售状态', '住宅类型', '标签', '价格'])
data['地址'] = data['地址'].str.replace('&nbsp;', '')

# 城市---小区数关系
print(data[['城市', '小区名']].groupby('城市').count())
# 只提取出均价数据
data['价格'] = data[data['价格'] != '售价待定']['价格']
data['价格'] = data[data['价格'].str.contains('均价').fillna(False)]['价格']
# print(data['价格'])
data['价格'] = data['价格'].str.replace('均价<span>','').str.replace('</span>元/㎡','')
# data['价格'] = data['价格']
# data['价格'] = data['价格'].str.replace('最低<span>','').replace('</span>元/㎡','')
# data['价格'] = data['价格'].str.replace('起','').replace('</span>元/㎡','')
# print(data['价格'].apply(lambda x:x if re.search("^\d+$", str(x)) else np.nan))
data['价格'] = data['价格'].astype('float')

# 城市----均价关系
city_price = data[['城市', '价格']].groupby('城市', as_index=False).mean().dropna().sort_values(by=['价格'], ascending=False)[: 10]
plt.title('全国城市房价TOP10')
plt.xlabel('城市')
plt.ylabel('均价')
plt.xticks(rotation=360)
plt.bar(city_price['城市'], city_price['价格'])
print('全国城市房价TOP10')
print(city_price)
plt.show()
# 建筑面积
data['建筑面积'] = data['户型'].str.split('：').str[1]
# 户型
data['户型'] = data['户型'].str.split('：').str[0].str.replace('建筑面积','')
print(data['户型'].str.split('：').str[0].str.replace('建筑面积','').str.split('/').str[1])
# 户型---均价关系表
type_price = data[['户型', '价格']].groupby('户型', as_index=False).mean().dropna().sort_values(by=['价格'], ascending=False)[:20]
print('全国不同户型房价TOP20')
print(type_price)
plt.title('全国不同户型房价TOP20')
plt.xlabel('户型')
plt.ylabel('均价')
plt.xticks(rotation=90)
plt.bar(type_price['户型'], type_price['价格'])
plt.show()
# 建筑面积---均价关系表

print(data[['建筑面积', '价格']].groupby('建筑面积').mean().dropna())

# 长株潭
c_z_t = data[data[['城市', '价格', '小区名', '销售状态']]['城市'].isin(['长沙', '株洲', '湘潭'])][['城市', '价格', '小区名', '销售状态']].dropna()
# 长株潭城市均价比较

czt_price = c_z_t[['城市', '价格']].groupby('城市', as_index=False).mean()
print('长株潭城市均价比较')
print(czt_price)
plt.title('长株潭城市均价比较')
plt.xlabel('城市')
plt.ylabel('均价')
plt.xticks(rotation=360)
plt.bar(czt_price['城市'], czt_price['价格'])
plt.show()
# 长株潭城市小区数量比较
czt_num = c_z_t[['城市', '小区名']].groupby('城市', as_index=False).count()
print('长株潭城市小区数量分布')
print(czt_num)
plt.title('长株潭城市小区数量分布')
plt.xlabel('城市')
plt.ylabel('小区数')
plt.xticks(rotation=360)
plt.pie(czt_num['小区名'], labels=czt_num['城市'], autopct='%1.2f%%')
plt.show()
# 长株潭城市小区价格排行
czt_name_price = c_z_t[['城市', '小区名', '价格']].sort_values(by=['城市', '价格'], ascending=False)
print('长株潭城市小区价格排行')
print(czt_name_price)
plt.title('长株潭城市小区价格排行')
plt.xlabel('城市')
plt.ylabel('价格')
plt.xticks(rotation=90)
# 长沙TOP10
cs_top10 = czt_name_price[czt_name_price['城市'].isin(['长沙'])][:10]
print('长沙TOP10')
print(cs_top10)
plt.subplot(221)
plt.title('长沙TOP10')
plt.ylabel('均价')
plt.xticks(rotation=90)
plt.bar(cs_top10['小区名'], cs_top10['价格'])
# 株洲TOP10
zz_top10 = czt_name_price[czt_name_price['城市'].isin(['株洲'])][:10]
print('株洲TOP10')
print(zz_top10)
plt.subplot(222)
plt.title('株洲TOP10')
plt.xticks(rotation=90)
plt.bar(zz_top10['小区名'], zz_top10['价格'])
# 湘潭TOP10
xt_top10 = czt_name_price[czt_name_price['城市'].isin(['湘潭'])][:10]
print('湘潭TOP10')
print(xt_top10)
plt.subplot(223)
plt.ylabel('均价')
plt.xlabel('小区名')
plt.title('湘潭TOP10')
plt.xticks(rotation=90)
plt.bar(xt_top10['小区名'], xt_top10['价格'])
# 长株潭TOP10
print('长株潭TOP10')
print(czt_name_price[:10])
plt.subplot(224)
plt.title('长株潭TOP10')
plt.xlabel('小区名')
plt.xticks(rotation=90)
plt.bar(czt_name_price['小区名'][:10], czt_name_price['价格'][:10])
plt.show()

# 长株潭在售数量
czt_zx = c_z_t[c_z_t[['城市', '销售状态']]['销售状态'].isin(['在售'])].groupby('城市').count()
print('长株潭在售数量')
print(czt_zx)

# 标签---均价关系表
# 标签格式化
trg_pirce = data[['标签', '价格']]
trg_split=trg_pirce['标签'].str.split('/')
trg_1=[trg_split.str[0],trg_pirce['价格']]
trg_2=[trg_split.str[1],trg_pirce['价格']]
trg_3=[trg_split.str[2],trg_pirce['价格']]
trg_4=[trg_split.str[3],trg_pirce['价格']]
# print(pd.DataFrame(trg_1).T)
# result = pd.concat([pd.DataFrame(trg_1),pd.DataFrame(trg_2),pd.DataFrame(trg_3),pd.DataFrame(trg_4)],axis=0,join='outer')
trg_price = pd.DataFrame(trg_1).T.dropna().append(pd.DataFrame(trg_2).T.dropna()).append(pd.DataFrame(trg_3).T.dropna()).append(pd.DataFrame(trg_4).T.dropna())
trg_price['价格'] = trg_price['价格'].astype('float')
trg_price = trg_price.groupby('标签').mean()

print(trg_price)