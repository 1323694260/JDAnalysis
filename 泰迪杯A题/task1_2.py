import pandas as pd
# 读取源数据
data = pd.read_csv("附件.csv", encoding='gbk', engine='python').dropna()
# 根据大类分组统计总销售金额
result = data[['大类编码', '大类名称', '销售金额']].groupby(['大类编码', '大类名称'], as_index=False).sum()
print(result)
result.to_csv('task1_2.csv', index=False)