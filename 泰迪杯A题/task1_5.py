import pandas as pd

data = pd.read_csv("附件.csv", encoding='gbk', engine='python')
# 时间格式化销售日期
data['销售日期'] = pd.to_datetime(data['销售日期'], format='%Y%m%d', errors='coerce')
# 提取销售日期中的月份
data['month'] = data['销售日期'].apply(lambda x: x.month)
# 提取销售日期中的日
data['消费天数'] = data['销售日期'].apply(lambda x: x.day)
# data['销售月份'] = pd.to_datetime(data['销售月份'], format='%Y%m')
# 根据顾客编号和销售月份分组统计顾客每月销售总额
product_month_price = data[['顾客编号', '销售月份', '销售金额']].groupby(['顾客编号', '销售月份'], as_index=False).sum()
# 分组统计顾客每月消费天数
product_month_day = data[['顾客编号', 'month', '消费天数']].groupby(['顾客编号', 'month'], as_index=False).count()
# 删除月份列
del product_month_day['month']
# 合并顾客每月销售总额和顾客每月消费天数
product_month_price['消费天数'] = product_month_day['消费天数']
# 提取用户1-10的数据
user_10 = product_month_price[product_month_price['顾客编号'].isin([i for i in range(11)])]
print(user_10)

# 写入csv
product_month_price.to_csv('task1_5.csv', index=False)
