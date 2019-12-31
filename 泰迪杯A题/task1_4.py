import pandas as pd

data = pd.read_csv("附件.csv", encoding='gbk', engine='python')
# 提取生鲜类和一般商品
result = data[data['商品类型'].isin(['生鲜', '一般商品'])].dropna()
# 将销售日期转为时间格式--方便计算   --
result['销售日期'] = pd.to_datetime(result['销售日期'], format='%Y%m%d', errors='coerce') # 设置异常为Nat
result = result.dropna()    # 删除时间格式异常的数据
# 计算销售日期的周数---计算结果为每年的第几周
result['销售日期'] = result['销售日期'].apply(lambda x: str(x.isocalendar()[0])+"年第"+str(x.isocalendar()[1])+"周")
# 分组统计每周销售总金额
result = result[['商品类型', '销售日期', '销售金额']].groupby(['商品类型', '销售日期'], as_index=False).sum()

print(result)
# 写入csv
result.to_csv('task1_4.csv', index=False)