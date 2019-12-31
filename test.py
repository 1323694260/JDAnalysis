k = input("请输入人数")
n = input("请输入灯数")
list=[]
for x in range(int(n)):
    list.append(0)

for i in range(1,int(k)+1):
    j=0
    while j<int(n):
        if(j%i==0):
            if(list[j]==0):
                list[j]=1
            else:
                list[j]=0
        j+=1
for i in range(int(n)):
    if list[i]==1:
        print(i)