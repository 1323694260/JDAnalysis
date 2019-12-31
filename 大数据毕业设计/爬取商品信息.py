import requests
from lxml import etree
import time
import csv
import random
import socket

socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
def main(url):
    headers = {
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/52.0.2743.116 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
    }
    response=None
    try:
        response = requests.get(url=url, headers=headers)
    except:
        response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.content.decode('utf-8'))
    price = html.xpath('//*[@class="p-price"]/strong/i/text()')
    product_urls = html.xpath('//*[@class="p-name p-name-type-2"]/a/@href')
    response.close()  # 关闭连接
    i = 0
    # 循环进入每个商品获取信息
    for product_url in product_urls:
        try:
            product = requests.get(url='http:' + product_url, headers=headers)
            product_html = etree.HTML(product.text)
            ''
            product_brand = product_html.xpath('//*[@id="parameter-brand"]/li/a/text()')[-1].strip()
            product_title = product_html.xpath('/html/body/div[6]/div/div[2]/div[1]/text()')[-1].strip()
            product_name = ''
            try:
                product_name = product_html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]/li[1]/text()')[-1].strip()
            except:
                product_name = product_html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]/text()')[-1].strip()
            product_SKU = ''
            try:
                product_SKU = product_html.xpath('// *[ @ id = "detail"] / div[2] / div[1] / div[1] / ul[3] / li[2]/text()')[-1].strip()
            except:
                product_SKU = product_html.xpath('// *[ @ id = "detail"] / div[2] / div[1] / div[1] / ul[2] / li[2]/text()')[-1].strip()
            comment_num_request = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + product_SKU.replace(
                '商品编号：', '')  # 评论数
            comment_num = requests.get(url=comment_num_request, headers=headers)

            product.close()  # 关闭连接
            p_comment = []
            time.sleep(random.randint(1, 3))  # 等待2秒
            for comment in comment_num.json()["CommentsCount"]:
                p_comment.append([comment["CommentCount"], comment["AverageScore"],
                                  comment["GoodCount"], comment["DefaultGoodCount"],
                                  comment["GoodRate"], comment["AfterCount"], comment["VideoCount"],
                                  comment["PoorCount"], comment["GeneralCount"]])
                # 总评数，平均得分，好评数，默认好评，好评率，追评数，视频晒单数，差评数，中评数
            print("正在写入-------------", product_title)
            with open('空气净化器.csv', 'a', newline='') as file:
                row = [product_title, product_brand, product_name.replace('商品名称：', ''),
                       product_SKU.replace('商品编号：', ''), price[i],
                       p_comment[0][0], p_comment[0][1], p_comment[0][2], p_comment[0][3], p_comment[0][4],
                       p_comment[0][5], p_comment[0][6], p_comment[0][7], p_comment[0][8]]
                write = csv.writer(file)
                # 标题 品牌 名称 SKU 价格 总评数，平均得分，好评数，默认好评，好评率，追评数，视频晒单数，差评数，中评数
                write.writerow(row)
            i += 1
        except:
            print("正在写入-------------", "异常信息")
            with open('空气净化器.csv', 'a', newline='') as file:
                row = ['', '', '',
                       '', '',
                       '', '', '', '', '',
                       '', '', '', '']
                write = csv.writer(file)
                write.writerow(row)
            i += 1
# 循环翻页---100页
for i in range(1, 200, 2):
    key = '空气净化器'
    url = 'https://search.jd.com/Search?keyword='+key+'&enc=utf-8&wq='+key+'&pvid=75f0597b31d943afa68a56913f2af44d&psort=4&stock=1&page=' + str(
        i) + "&s=61&click=0"
    print("第", i, '页')
    print(url)
    main(url)
