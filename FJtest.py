import requests
import re
from lxml import etree
import csv


def start(city,url):
    # 谷歌浏览器请求头
    hander = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    # 网页请求开始
    html = requests.get(url,headers=hander)
    # 获取网页内容
    context = html.text
    # 标题---正则
    title = re.findall('class="items-name">(.*)</span>',context)
    # 地点---正则
    map = re.findall('class="list-map" target="_blank">(.*)</span>',context)
    # 解析html成节点 使用xpath表达式
    html = etree.HTML(context)
    # 户型 和建筑面积  --xpath
    html_get = html.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div')
    # 创建户型和建筑面积数组
    apartment_S_list = []
    # 创建标签组
    tagers = []
    # 遍历获取每个数据的户型和建筑面积
    for l in html_get:
        # 获取每个户型的数据
        apartment = l.xpath('div/a[3]/span/text()')
        # 拼接
        apartment_S_list.append('/'.join(apartment))
        # 获取每个房子的标签
        tager = l.xpath('div/a[4]/div/span/text()')
        tagers.append('/'.join(tager))

    # 销售状态
    sale_state = html.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div/div/a[4]/div/i[1]/text()')
    # 类型
    type = html.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div/div/a[4]/div/i[2]/text()')

    # 均价  //*[@id="container"]/div[2]/div[1]/div[3]/div[1]/a[2]/p[1]
    #price = html.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div/a[2]/p[1]/span/text()')
    price = re.findall('class="price">(.*)</p>|class="price-txt">(.*)</p>',context)

    # 联系电话
    # tel = html.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div/a[2]/p[2]/text()')
    tel = re.findall('class="tel">(.*)<i',context)


    # 地区
    # region = html.xpath('//*[@id="header"]/div[3]/div[2]/div/dl/dt/text()')
    # print(region)
    # 获取城市
    # city_name = html.xpath('//*[@id="header"]/div[3]/div[2]/div/dl/dd/a/text()')
    # city_url = html.xpath('//*[@id="header"]/div[3]/div[2]/div/dl/dd/a/@href')
    # print(city_name)
    # print(city_url)


    # print(len(title), title)#标题
    # print(len(map), map)#地址
    # print(len(apartment_S_list), apartment_S_list)#户型
    # print(len(sale_state), sale_state)#销售状态
    # print(len(type), type)# 住宅类型
    # print(len(tagers), tagers)#标签
    # print(len(price), price)#价格
    # print(len(tel), tel)#联系电话
    writeData(city,title,map,apartment_S_list,sale_state,type,tagers,price)

    # 获取下一页超链接
    next_url = html.xpath('//*[@id="container"]/div[2]/div[1]/div[4]/div/a[@class="next-page next-link"]/@href')
    print(next_url)
    if next_url:
        start(city, next_url[0])

def writeData(city,title,map,apartment_S_list,sale_state,type,tagers,price):
        f= open("FjData-test.csv", 'a',encoding='utf8',newline='')
        for i in range(len(title)):
            # 价格数据  格式化     ('均价<span>5700</span>元/㎡', '')
            price[i]=price[i][0] if price[i][0] else price[i][1]
            try:
                row = [city, title[i],map[i],apartment_S_list[i],sale_state[i],type[i] ,tagers[i],price[i]]
            except:
                # 超出索引异常处理
                title.append('')
                map.append('')
                apartment_S_list.append('')
                sale_state.append('')
                type.append('')
                tagers.append('')
                price.append('')
                row = [city, title[i], map[i], apartment_S_list[i], sale_state[i],type[i], tagers[i], price[i]]
            print(apartment_S_list[i])
            write = csv.writer(f)
            write.writerow(row)
        f.close()
if __name__ == '__main__':
    index = 'https://zhuzhou.anjuke.com/'
    # 安居客 株洲新房 url
    start_url = 'https://zhu.fang.anjuke.com/?from=navigation'

    with open("city.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line:
                # 所有城市的名称和链接放入，开始抓取数据
                start(line[0],line[1])
    # start(start_url)