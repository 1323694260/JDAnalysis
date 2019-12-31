import pandas as pd
import jieba
import operator
from functools import reduce
from pyecharts.charts import wordcloud
def tiqu_data(x):
    if len(x) >= 2:
        return x
def main(file, data):
    c = []
    # 分词提取词
    data['content'].apply(lambda x: c.append(list(jieba.cut(x))))
    # 二维转一维
    c = reduce(operator.add, c)
    c = pd.DataFrame(c, columns=['name'])
    c['value'] = pd.DataFrame(c)
    # 只取长度大于等于2的词
    c['name'] = c['name'].apply(lambda x: tiqu_data(x))
    c['value'] = c['name']
    # 分组统计排序
    word_count = c.groupby('name', as_index=False).count().sort_values('value', ascending=False)[:150]
    return word_count


def word_cloud(file,word_count_data):
    # 绘制词云图
    cloud = wordcloud.WordCloud(width=1800, height=800)
    cloud.add("用户典型意见", word_count_data['name'], word_count_data['value'])
    cloud.render(file+"用户典型意见.html")
if __name__ == '__main__':
    # file = '../小米2s评论.csv'
    # file = '../飞利浦评论.csv'
    file = '../松下评论.csv'
    data = pd.read_csv(file, encoding='gbk')
    word_count_data = main(file, data)
    word_cloud('松下评论', word_count_data)