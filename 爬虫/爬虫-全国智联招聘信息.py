import requests
from lxml import etree
import re
import json
import csv
import time
header = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
    "cookie":"dywea=95841923.375121788475447700.1539841809.1571124375.1571129552.21; dywez=95841923.1571129552.21.18.dywec"
             "sr=baidu|dyweccn=(organic)|dywecmd=organic; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221015818437%22%"
             "2C%22%24device_id%22%3A%2216685b959f111d-0a67cdf1c755ab8-4c312878-1327104-16685b959f23b5%22%2C%22props%22%3A%7"
             "B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24l"
             "atest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.co"
             "m%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%2"
             "2%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22hydt%22%2C%22%24"
             "latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228719918%22%7D%2C%22first_id%22%3A%2216685b959"
             "f111d-0a67cdf1c755ab8-4c312878-1327104-16685b959f23b5%22%7D; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1569748120"
             ",1569748128,1571124375,1571129552; sts_deviceid=16685b95a609-07b4d65b39da568-4c312878-1327104-16685b95a62546; _"
             "jzqa=1.1379152549729831000.1539841809.1556087279.1558259205.6; __xsptplus30=30.5.1552652713.1552652713.1%232%7C"
             "bzclk.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23Tykw6eX9bF4qmXLjKn"
             "ENa8SCGwT0i0zw%23; dywem=95841923.y; Hm_lvt_80e552e101e24fe607597e5f45c8d2a2=1552652996,1552653105,1552653258,1"
             "552653315; zg_did=%7B%22did%22%3A%20%2216685d052d0215-00a8c8f1278e678-4c312878-144000-16685d052d3269%22%7D; zg_"
             "08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201539843314406%2C%22updated%22%3A%201539843314880%2C%22info%22"
             "%3A%201539843314422%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20"
             "%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; __utma=269921210.328470850.1540114360.1571124377.1571129552."
             "19; __utmz=269921210.1571129552.19.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; user_id=1032297231; zp-auth=6"
             "018ceca79da4d0ea6660ef453b682a9; _jzqx=1.1556087279.1558259205.2.jzqsr=jobs%2Ezhaopin%2Ecom|jzqct=/cz808308570j00"
             "068426711%2Ehtm.jzqsr=zhaopin%2Ecom|jzqct=/; x-zp-client-id=db16be95-6fe3-4347-8cf5-c2e961f08021; select_city_cod"
             "e=750; select_city_name=%E6%A0%AA%E6%B4%B2; urlfrom2=121114583; adfcid2=www.baidu.com; adfbid2=0; sou_experiment=c"
             "api; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; acw_tc=2760826315688656736684035eaa4b7086210a69d718a70bdde2d2"
             "555c544a; urlfrom=121114583; adfcid=www.baidu.com; adfbid=0; dywec=95841923; Hm_lpvt_38ba284938d5eddca645bb5e02a02"
             "006=1571129971; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DY4BHITt5_VMHB"
             "J7jxX3Mna2f2TJzDQjQz7HsZvYappOL_wPyb0H-J-SlvLD7tmb9%26wd%3D%26eqid%3D9278cc600006fc19000000055da5748f; jobRiskWarn"
             "ing=true; __utmc=269921210; dyweb=95841923.1.10.1571129552; __utmb=269921210.1.10.1571129552; __utmt=1; sts_evtseq"
             "=9; sts_sid=16dce9e6f4d276-0ea8e820ebe4ab8-4c312373-1327104-16dce9e6f4e116; ZL_REPORT_GLOBAL={%22sou%22:{%22action"
             "id%22:%2236409673-f428-491a-92ba-6aa1510e3e00-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recom"
             "mandActionidShare%22:%227aebb8bb-1471-4ae3-9805-4911f2a1c120-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}"
             "; ZP_OLD_FLAG=false; POSSPORTLOGIN=8; CANCELALL=0"
}


def get_context(number):
    url = "https://fe-api.zhaopin.com/c/i/similar-positions?number="+number


    urll='https://jobs.zhaopin.com/'+number+'.htm'
    html = requests.get(url=url)
    # print(html.json()['data']['data']['list'])
    companyName,companyNumber,companySize,salary60,workCity,education,\
    workingExp,property,companyUrl,positionURL,name,welfareLabel,number,cityId,cityDistrict,applyType,score,tag="","","","","","","","","","","","","","","","","",""
    try:
        for i in html.json()['data']['data']['list']:
            companyName = i['companyName']  # 公司
            companyNumber = i['companyNumber']  # ID
            companySize = i['companySize']  # 规模
            salary60 = i['salary60']  # 薪水
            workCity = i['workCity']  # 城市
            education = i['education']  # 学历
            workingExp = i['workingExp']  # 工作经验
            property = i['property']  #企业性质
            companyUrl = i['companyUrl']  # 公司网址
            positionURL = i['positionURL']  # 求职网址
            name = i['name']  # 职位名称
            # welfareLabel = i['welfareLabel']  # 福利
            number = i['number']  # 编号
            cityId = i['cityId']  # 城市id
            cityDistrict = i['cityDistrict']  # 城市区域
            applyType = i['applyType']  # 公司类型
            score = i['score']  # 公司分数
            tag=[] #标签

            for j in i['welfareLabel']:
                tag.append(j['value'])
            tag="/".join(tag)
    except:
        pass

    html = requests.get(url=urll, headers=header)
    html_xpath = etree.HTML(html.text)
    # miaosu = re.findall('<div class="describtion__detail-content">(.*?)</div></div><div class="job-address clearfix">', html.text)
    miaosu = html_xpath.xpath('string(//*[@class="describtion__detail-content"])')      # 提取子标签所有文本
    print("----------------------"+miaosu)
    miaosu = ''.join(miaosu)
    # time.sleep(1)
    fp = open('智联招聘.csv', 'a', newline='')
    write = csv.writer(fp)
    row = (companyName,name, tag ,companyNumber ,companySize, salary60,workCity,education,workingExp,property,companyUrl,positionURL,name,number,cityId,cityDistrict,applyType,score,miaosu)
    write.writerow(row)
    print('正在写入----'+workCity+'----的职位数据'+'----------'+name)
    fp.close()



def get_url(city):
    key = 'python'      # 搜索关键字

    url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=4000&cityId='+city+'&kw='+key+'&kt=1'

    number  = ''
    url_head = 'https://jobs.zhaopin.com/'

    html = requests.get(url = url)
    try:
        for i in html.json()['data']['results']:
            print("-----------"+i['number'])
            # header['cookie'] = header.get('cookie')[0:-27] + i['number'] + ".htm"       # 动态设置cookie
            get_context(i['number'])          # 内容爬虫开始---/
            # print(url_head+i['number']+'.htm')
    except:
        pass


url = 'https://sou.zhaopin.com/?jl=852&sf=0&st=0&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3'
html = requests.get(url = url, headers = header).text
data =re.findall('<script>__INITIAL_STATE__=(.*?)</script>', html)
datas = json.loads(data[0])
try:
    for i in datas["basic"]["dict"]["location"]["province"]:
        # print(i["name"],end="  ")
        # print(i["code"])
        get_url(i["code"])
except:
    pass

