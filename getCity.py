import requests
from lxml import etree
import csv
# start_url = 'https://zhu.fang.anjuke.com/?from=navigation'
start_url = 'https://www.anjuke.com/sy-city.html'

hander = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
# 网页请求开始
html = requests.get(start_url,headers=hander)
# 获取网页内容
context = html.text
# 解析html成节点 使用xpath表达式
html = etree.HTML(context)
# 获取城市
# city_name = html.xpath('//*[@id="header"]/div[3]/div[2]/div/dl/dd/a/text()')
# city_url = html.xpath('//*[@id="header"]/div[3]/div[2]/div/dl/dd/a/@href')

city_name = html.xpath('/html/body/div[3]/div/div[2]/ul/li/div/a/text()')
city_url = html.xpath('/html/body/div[3]/div/div[2]/ul/li/div/a/@href')

with open("city.csv", 'w+',newline='') as f:
    for i in range(len(city_name)):
        # 城市链接 的新房链接规律
        flag = city_url[i].split('.')
        # 标准url  等会记得改  添加一个loupan
        # https://as.fang.anjuke.com/loupan/all/p2/
        city_url[i] = flag[0]+'.fang.' + flag[1]+'.'+flag[2]+'/loupan'
        row = [city_name[i], city_url[i]]
        print(row)
        write = csv.writer(f)
        write.writerow(row)
    print("写入完毕！")
