import requests
from requests.cookies import RequestsCookieJar

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
        "Referer": "https://www.baidu.com/s?wd=%BC%96%E7%A0%81&rsv_spt=1&rsv_iqid=0x9fcbc99a0000b5d7&issp=1&f=8"
                   "&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=If-None-Match&inputT=7282"
                   "&rsv_t=3001MlX2aUzape9perXDW%2FezcxiDTWU4Bt%2FciwbikdOLQHYY98rhPyD2LDNevDKyLLg2&rsv_pq"
                   "=c4163a510000b68a&rsv_sug3=24&rsv_sug1=14&rsv_sug7=100&rsv_sug2=0&rsv_sug4=7283",
        "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
        'cookie':'fdsf=442343'
    }
html = requests.get(url='http://jobs.zhaopin.com/CC879864350J00334868005.htm' , headers=headers)
cookie = RequestsCookieJar(html.cookies)
print(cookie.items())
print(html.text)