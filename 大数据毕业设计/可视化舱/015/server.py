from flask import Flask
from flask import render_template
import pandas as pd
from flask import request
from flask import session
# 各大品牌销量排行榜
def commentTop(data, sku):
    # 去掉米家后面的（MIJIA）
    data['品牌'] = data['品牌'].str.replace('（MIJIA）', '')
    # 取出评论数前十的产品
    name_comment = data[['标题', '总评数']].groupby('标题', as_index=False).mean().sort_values(by=['总评数'], ascending=False)
    # 按评论数排行的进入TOP10的品牌产品数量
    brand_num_top10 = data[data['标题'].isin(name_comment['标题'])][['品牌', '总评数']].groupby('品牌',
                                                                                       as_index=False).count().sort_values(
        by=['总评数'], ascending=False)
    brand_comment = data[['品牌', '总评数']].groupby('品牌', as_index=False).sum().sort_values(by=['总评数'], ascending=False)
    # print(brand_comment)
    p_bard = data[data['SKU'].isin([sku])]['品牌']
    # return (brand_comment) # 十大品牌
    # return (brand_num_top10) # 十大型号品牌分布
    # 取前100
    return (p_bard, brand_comment[:100])
# 品牌畅销型号销量对比分析
def brand_xinghao(data, sku):
    data['品牌'] = data['品牌'].str.replace('（MI）''|''（MIJIA）''|''（PHILIPS）''|''（Honeywell）''|''（Blueair）''|''（Panasonic）',
                                       ' ').dropna()
    data['品牌'] = data['品牌'].str.replace('米家', '小米').str.strip()
    data = data.sort_values(by='总评数', ascending=False).drop_duplicates()
    # name = ['小米', '飞利浦', '松下']
    commodity_x = []
    sales_y = []
    price = []
    # 筛选出前3品牌所有信息 ['总评数','好评数','追评数','差评数']
    # 取前100
    commodity_x.append(list(data['名称'][:100]))
    sales_y.append(list(data['总评数'][:100]))
    price.append(list(data['价格'][:100]))
    from itertools import chain
    commodity_x = list(chain(*commodity_x))
    sales_y = list(chain(*sales_y))
    price = list(chain(*price))
    p_bard = data[data['SKU'].isin([sku])]['名称']
    p_bard = list(p_bard)[0]
    print(p_bard)
    return {
        'id': p_bard,
        'x': list(commodity_x),
        'y_bar': list(sales_y),
        'y_line': list(price)
    }
# 销量TOP10型号品牌分布
def sales_top10_brand(data, sku):
    # 去掉米家后面的（MIJIA）
    data['品牌'] = data['品牌'].str.replace('（MIJIA）', '')
    # 取出评论数前十的产品
    name_comment = data[['标题', '总评数']].groupby('标题', as_index=False).mean().sort_values(by=['总评数'], ascending=False)[
                   :10]
    # 按评论数排行的进入TOP10的品牌产品数量
    brand_num_top10 = data[data['标题'].isin(name_comment['标题'])][['品牌', '总评数']].groupby('品牌',
                                                                                       as_index=False).count().sort_values(
        by=['总评数'], ascending=False)
    p_bard = data[data['SKU'].isin([sku])]['品牌']
    p_bard = list(p_bard)[0]
    print(p_bard)
    # 十大型号品牌分布
    return {
        'id': p_bard,
        'x': list(brand_num_top10[:10]['品牌']),
        'y': list(brand_num_top10[:10]['总评数'])
    }

# 各品牌商家数量分布  叉叉叉
def brand_tore_num(data, sku):
    data['标题'] = data['标题'].apply(lambda x: str(x)[:6])
    data = data[['标题', 'SKU']].groupby('标题', as_index=False).count()
    p_bard = data[data['SKU'].isin([sku])]['标题']
    print(data)

# 用户正面评论趋势
def user_score(data, sku):
    data['score'] = data['score'].astype('int')  # 转int
    data['reference_time'] = pd.to_datetime(data['reference_time'])  # 转时间
    data = data.sort_values(by='reference_time')  # 根据时间排序
    z = data[data['score'] > 4]  # 评分大于或等于4星为正面
    f = data[data['score'] <= 4]  # 评分小于4星为负面
    z_plot = z[['reference_time', 'score']].groupby(z['reference_time'].dt.date).count()
    f_plot = f[['reference_time', 'score']].groupby(f['reference_time'].dt.date).count()
    return {
        'x': list(z_plot.index),
        'y': list(z_plot['score']),
        'y_f': list(f_plot['score'])
    }

# 用户情感--好评差评对比
def user_score_star(data, sku):
    # good_comment1 = [sum(data[data['SKU'].str.contains(sku)]['总评数'])]
    # centre_comment1 = [sum(data[data['SKU'].str.contains(sku)]['好评数'])]
    # check_comment1 = [sum(data[data['SKU'].str.contains(sku)]['差评数'])]
    # chase_comment1 = [sum(data[data['SKU'].str.contains(sku)]['追评数'])]
    # print(data['SKU'])
    good_comment = list(data[data['SKU'].isin([sku])]['好评数'])[0]
    check_comment = list(data[data['SKU'].isin([sku])]['差评数'])[0]
    item = []
    item.append(good_comment)
    item.append(check_comment)
    # 好评率:好评人数/总评价人数
    # feedback1 = [centre_comment1[i]/good_comment1[i] for i in range(3)]
    # feedback1 = [((centre_comment1[i] - check_comment1[i]) + chase_comment1[i]) / good_comment1[i] for i in range(3)]
    # print('小米2S,飞利浦AC4076,松下F-PDF35C-G各综合得分：', feedback1)
    # 指定评价等级和评价标准
    # 先制定出各项评价指标，统一的评价等级，分值范围
    # 偏差率 = 100% * （投标人评标价-评标基准价）/评标基准价
    # （好评-差评）*50 + 追评 *50 /总评论 = 综合得分
    # 个商品综合得分 = 好评 *77.27% + 追评* 0.34% + 晒单*0.59%+ 差评*0.179%+中评+0.179% + 未评价（75,495）‬*21.26%#
    print(item)
    print(item[0] / sum(item))

    return {
        'x': ['好评数', '差评数'],
        'y': item
    }

def tiqu_data(x):
    if len(x) >= 2:
        return x

# 用户典型意见
def user_opinion(data, sku):
    import operator
    from functools import reduce
    import jieba
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
    return {
        'x': list(word_count['name']),
        'y': list(word_count['value'])
    }


# 用户总评数----综合得分
def tal_score(data, sku):
    print(data[data['SKU'].isin([sku])])
    good_comment = list(data[data['SKU'].isin([sku])]['好评数'])[0]
    check_comment = list(data[data['SKU'].isin([sku])]['差评数'])[0]
    zhui_comment = list(data[data['SKU'].isin([sku])]['追评数'])[0]
    tal_comment = list(data[data['SKU'].isin([sku])]['总评数'])[0]
    title = list(data[data['SKU'].isin([sku])]['名称'])[0]
    # 偏差率 = 100% * （投标人评标价-评标基准价）/评标基准价
    # （好评-差评）*50 + 追评 *50 /总评论 = 综合得分
    zon = (good_comment - check_comment + zhui_comment) / tal_comment
    return {
        'name': title,
        'tal_comment': tal_comment,
        'zon_score': zon
    }


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '123456'

# 跨域问题
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


# 品牌销量对比
@app.route('/brand_Sales')
def brand_Sales():
    sku = session.get('sku')
    # product_info = 'templates/商品信息.csv'
    product_info = session.get('product_info_path')
    data = pd.read_csv(product_info, encoding='gbk')
    try:
        c_Top10 = commentTop(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'
    print(list(c_Top10[0])[0])
    return {
        'id': list(c_Top10[0])[0],
        'x': list(c_Top10[1]['品牌']),
        'y': list(c_Top10[1]['总评数'])
    }


# 品牌畅销型号销量与价格对比
@app.route('/brand_Sales_price')
def brand_Sales_price():
    sku = session.get('sku')
    # product_info = 'templates/商品信息.csv'
    product_info = session.get('product_info_path')
    data = pd.read_csv(product_info, encoding='gbk')
    try:
        return brand_xinghao(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'


# 销量TOP10型号品牌分布
@app.route('/sales_top10_brand')
def url_sales_top10_brand():
    sku = session.get('sku')
    # product_info = 'templates/商品信息.csv'
    product_info = session.get('product_info_path')
    data = pd.read_csv(product_info, encoding='gbk')
    try:
        return sales_top10_brand(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'


# 用户正面评分趋势
@app.route('/user_score')
def url_user_score():
    sku_path = session.get('sku_path')
    sku = session.get('sku')
    data = pd.read_csv(sku_path, encoding='gbk')
    try:
            return user_score(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'


# 用户情感--好评差评对比
@app.route('/user_score_star')
def url_user_score_star():
    sku = session.get('sku')
    # product_info = 'templates/商品信息.csv'
    product_info = session.get('product_info_path')
    data = pd.read_csv(product_info, encoding='gbk')
    try:
        return user_score_star(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'

# 用户典型意见
@app.route('/user_opinion')
def url_user_opinion():
    # sku = '5487565'
    sku_path = session.get('sku_path')
    sku = session.get('sku')
    # product_info = 'templates/商品信息.csv'
    # product_info = 'templates/' + session.get('product_info') + '.csv'
    data = pd.read_csv(sku_path, encoding='gbk')
    try:
        return user_opinion(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'


# 用户总评数----综合得分---主页
@app.route('/index')
def index():

    # sku = '5487565'
    sku_path = session.get('sku_path')
    sku = session.get('sku')
    # product_info = 'templates/商品信息.csv'
    product_info = session.get('product_info_path')
    # print('-----'+sku+product_info)
    data = pd.read_csv(product_info, encoding='gbk')
    try:
        d = tal_score(data, sku)
    except:
        return '<script>alert("抱歉，你的输入的SKU不存在");location.href="/login"</script>'
    #     pass
    zon_score = '{0:.8f}'.format(d['zon_score'])  # 取小数点后八位
    return render_template('index.html', name=d['name'], tal_comment=d['tal_comment'], zon_score=zon_score, sku_path=sku_path)


# 爬取商品评论信息
@app.route('/spider_comment', methods=['GET', 'POST'])
def url_spider_comment():
    import os
    file_dir = r"comment"
    i = 1
    a = os.walk(file_dir)
    files = None
    for root, dirs, files in os.walk(file_dir):
        i += 1
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件
    # 获取评论文件名
    print(files)
    files = [i.replace('.csv', '') for i in files]
    sku = session.get('sku')
    # 判断用户输入sku是否存在---存在则直接分析---不存在则爬取
    print('-------------')
    print(sku)
    print(files)
    if sku in files:
        print(12)
        return '<script>location.href="/index"</script>'
    else:
        productId = int(sku)
        from spider_comment import JDCommentsCrawler
        # 设置关键变量
        page = 100  # 页数
        # productId = 5487565  # 商品ID
        # productId = 100002866897  # 商品ID
        # productId = 298104  # 商品ID
        callback = 'fetchJSON_comment98vv12949'  # 回调函数
        JDC = JDCommentsCrawler(productId, callback, page)
        JDC.concatLinkParam()
        # 开始爬虫
        try:
            JDC.crawler()
        except:
            pass
        page = pd.DataFrame()
        for i in range(0, 100):
            try:
                df = pd.read_csv("user/%d.csv" % i, encoding="gbk")
                page = pd.concat([page, df], axis=0, ignore_index=True)
            except:
                pass
        # print(page['product_id'][0])
        page.to_csv('static/comment/' + str(productId) + '.csv', encoding='gbk')
        return '<script>location.href="/index"</script>'

# 获取已有的关键字搜索商品数据列表
@app.route('/login')
def getProductKey_data():
    import os
    file_dir = r"templates/product_info"
    i = 1
    a = os.walk(file_dir)
    files = None
    for root, dirs, files in os.walk(file_dir):
        i += 1
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件

    files = [i.replace('.csv', '') for i in files]
    return render_template('welcome.html', files=files)


# 登录开始---获取表单数据---商品关键字 and 商品SKU
@app.route('/start')
def start():
    # session设置
    session.permanent = True
    product_info = request.args['product_info']
    sku = request.args['sku']
    print(product_info,sku)
    session['product_info_path'] = 'templates/product_info/'+product_info+'.csv'
    session['sku_path'] = 'static/comment/'+sku+'.csv'
    session['sku'] = sku
    # print(session.get('product_info_path'))
    # return '<script>location.href="/spider_comment"</script>'
    return render_template('jjj.html')

if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0')
    sku = '5487565'
    # data = pd.read_csv('../商品信息.csv', encoding='gbk')
    # data = pd.read_csv(sku+'.csv', encoding='gbk')
    # user_score_star(data, sku)
