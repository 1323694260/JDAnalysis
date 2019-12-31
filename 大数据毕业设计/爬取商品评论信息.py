import requests
import time
from lxml import etree
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400 '
    }

for page in range(1):
    time.sleep(3)
    # request = requests.get(url="https://sclub.jd.com/comment/productPageComments.action?&productId=57161592832&score=0&sortType=5&page="+str(page)+"&pageSize=10&isShadowSku=0&fold=1", headers=headers)
    request = requests.get(url="https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv12949&productId=5487565&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1", headers=headers)
    print(request.text)
    # html = etree.HTML(request.text)
    # print(html.xpath('// *[ @ id = "comment-0"] / div[1] / div[2] / p'))

    # for i in request.json()['comments']:
    #     print(i['id'])  # id
    #     print(i['guid'])    # 用户id
    #     print(i['content'])     # 内容
    #     print(i['creationTime'])        # 评论时间
    #     print(i['isTop'])   # 是否置顶
    #     print(i['score'])   # 评分
    #     print(i['productColor'])    # 商品颜色
    #     print(i['productSize'])     # 商品规格
    #     print(i['referenceId'])     # 商品SKU
    #     print(i['referenceTime'])   # 追评时间
    #     print(i['nickname'])    # 用户名称
    #     print(i['referenceName'])   # 商品标题
    #     print('----------------------------')

