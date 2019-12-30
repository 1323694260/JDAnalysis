import os
file_dir = r"templates/product_info"
i = 1
a = os.walk(file_dir)
files = None
for root, dirs, files in os.walk(file_dir):
    i += 1
    # print(root) #当前目录路径
    # print(dirs) #当前路径下所有子目录
    print(files) #当前路径下所有非目录子文件

files = [i.replace('.csv', '') for i in files]
print(files)
import pandas as pd
page = pd.DataFrame()
for i in range(0, 100):
        try:
            df = pd.read_csv("comment/user/%d.csv" % i, encoding="gbk")
            page = pd.concat([page, df], axis=0, ignore_index=True)
        except:
            pass
# print(page['product_id'][0])
page.to_csv('comment/' + str(100009128964) + '.csv', encoding='gbk')