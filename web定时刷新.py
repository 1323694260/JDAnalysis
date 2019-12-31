import webbrowser
import time,os

num = 1
#num控制打开多少次，这个是100000次
while num <=100000:
    num += 1
    #控制多长时间打开一次
    time.sleep(60)
    webbrowser.open("https://as.fang.anjuke.com/loupan/all/p2/", 0, False)
    print('第',num)