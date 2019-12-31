import pandas as pd

data = pd.read_csv("附件.csv", encoding='gbk', engine='python')

# 数量取绝对值 避免负数数据
data['销售数量'] = data['销售数量'].abs()
data['销售金额'] = data['销售金额'].abs()
data['商品单价'] = data['商品单价'].abs()
# 将销售日期转为时间格式--方便计算   --
data['销售日期'] = pd.to_datetime(data['销售日期'], format='%Y%m%d', errors='coerce') # 设置异常为Nat
result = data.dropna()    # 删除时间格式异常的数据
print(result)
result.to_csv('task1_1.csv', index=False)



