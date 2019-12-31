import requests
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'shshshfpb=iv6b4kCftInaxg7uN0CODEg%3D%3D; shshshfpa=ccb001e6-0225-b49e-fc7b-8cef43a401ae-1569374359; __'
                  'jdu=15693743586532004551286; user-key=d41c7d1a-c076-4a30-9593-947425a61664; cn=1; PCSYCityID=CN_430000'
                  '_430200_430202; areaId=18; ipLoc-djd=18-1488-29447-0; unpl=V2_ZzNtbUdRRhRwCk5VKR9UUGIDE1kRUUpAfA5PUXkeV'
                  'AAwUUIJclRCFX0URlVnGVkUZwcZWEJcQRVFCEVkexhdBGELE1VGVnMlRQtGZHopXAFgCxBbR1VHHHIMRFd6GFkBYwMRVEVncxJ1AXZk'
                  'cxxbUD4zE21DZ0MSdA5FXXobVQ1XSHxcD1dHEn0KQFF5HVUCYwERXENSRxF1C09TSxhsBg%3d%3d; __jdv=76161171|kong|t_100'
                  '0790950_|tuiguang|47404390c79d4105b78d87843694fcae|1571038891523; __jda=122270672.1569374358653200455128'
                  '6.1569374359.1571038892.1571140880.19; __jdc=122270672; mt_xid=V2_52007VwMWVVVaVF8dTRBbAWUAE1NYXFZaHEAebA'
                  '1mCkUFVQwGRk1BSQ4ZYlNHWkEIWl8cVR1VAG9RFVpYCgVdFnkaXQVvHxJTQVhWSxxIEl0FbAAUYl9oUmoXTRBZB2YBFVVtWFReGw%3D%3'
                  'D; shshshfp=a92e9c04140d606bc6731c184466272c; _gcl_au=1.1.338227126.1571140889; 3AB9D23F7A4B3C9B=DAT53VYXQ'
                  'ZB4OOAAPJL6MMXG7AN4U7NXOXXBRAUXHWXJLV6QWRWBTQU33EACYZDGD7AVQ5QZH5UZKYWU5L4Z5LENIQ; __jdb=122270672.12.1569'
                  '3743586532004551286|19.1571140880; shshshsID=069042ac37b5c6742867f97782949bbb_10_1571142681320',
        'Host': 'sclub.jd.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400 '
    }

url = 'https://review.suning.com/ajax/cluster_review_lists/general-30202453-000000010598643045-0000000000-total-1-default-10-----reviewList.htm?callback=reviewList/'
html = requests.get(url, headers=headers)
print(html.text)