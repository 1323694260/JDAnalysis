import pandas as pd
page = pd.read_csv("../3/0.csv", encoding="gbk")
for i in range(1, 100):
    try:
        df = pd.read_csv("../3/%d.csv" % i, encoding="gbk")
        page = pd.concat([page, df], axis=0, ignore_index=True)
    except:
        break
print(page['product_id'][0])
page.to_csv('松下评论.csv', encoding='gbk')