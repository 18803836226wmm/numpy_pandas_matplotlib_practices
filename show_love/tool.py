import pandas as pd
import re

data=open('love_test.txt')
ll=data.readlines()
data.close()
print(ll)
txt=open('love.txt','w')
data_new=[]
for i in ll:
    # hh=str(i).split(' ',1)
    # data_new.append(hh[1])
    aa=i[2:]
    data_new.append(aa)
for aa in data_new:
    txt.write(aa)



# 二维数组只有一列时，列的名称需要加中括号
# for i in data_new:
#     test=pd.DataFrame(data=i)
#     test.to_csv('pig.csv',encoding='utf-8', mode='a', index = False, header = False)

