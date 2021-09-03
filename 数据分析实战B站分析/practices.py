import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#读取单个文件下的数据记录
# data=pd.read_excel('./data/bilibili2月8日订单.xlsx')
# print(data.head())
file_path='./data'
file_list=os.listdir(file_path)
print(file_list)
data_all=[]
for order in file_list:
    # print(file_path+"/"+order)
    data_all.append(pd.read_excel(file_path+"/"+order))
    # print(data.head())
print(data_all)
print(data_all.shape)

