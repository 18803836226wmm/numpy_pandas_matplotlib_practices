"""
1.loc 使用标签索引的方式（index,和columns） 都是标签
2.iloc 方法利用位置来进行选取，与loc用法类似，只不过使用的是位置索引不是标签索引
3.ix()混合索引 用法与loc、iloc一样 只不过既能用标签索引，也能用位置索引
"""
import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randint(0,10,[3,4]),
                index=np.arange(0,3),columns=['a','b','c','d'])
print(df)
# 访问某个值
print(df.loc[0,'b'])
# 访问某列值， ；分号代表取完所有行
print(df.loc[:,'b'])
# 访问 某些列 数据比较多用数组
print(df.loc[:,['b','c']])
# 访问index为1，往后的所有行的b列
print(df.loc[1:,'b'])
# 访问index0，2的行，colums为b、c的列
print(df.loc[[0,2],['b','c']])
# 访问某个值
print(df.iloc[0,0])
#访问某列 第0列
print(df.iloc[:,0])
# 访问某几列
print(df.iloc[:,])