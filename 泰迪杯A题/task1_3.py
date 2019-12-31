import pandas as pd

data = pd.read_csv("附件.csv", encoding='gbk', engine='python').dropna()
# 根据中类和是否促销分组统计总销售金额
result = data[['中类编码', '中类名称', '销售金额', '是否促销']].groupby(['中类编码', '中类名称', '是否促销'], as_index=False).sum()

print(result)
result.to_csv('task1_3.csv', index=False)