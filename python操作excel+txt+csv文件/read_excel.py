import pandas as pd
"""
pd.read_exce()参数
sheet_name:EXCEL文件中的表名
index_col:使用那一列作为索引，默认从0开始
usecils：读取表格中的那几列，必须是位置索引
header:哪一行设置为索引，默认是第一行，即 header=0
data_parser:解析日期的函数
skiprows:跳过前几行读取文件
"""
def read01_excel_data():
    file_path='邮件模板.xlsx'
    df=pd.read_excel(file_path,sheet_name='主编信件',index_col=1,header=0,skiprows=2,nrows=10)
    df2 = pd.read_excel(file_path, sheet_name='变量', index_col=0, header=0)
    print(df)
    """1。读取excel的单列数据，返回list"""
    print(df['事件'])# 返回的是一个list集合
    title_list1=df['事件'].tolist()
    title_list2=df['模板ID'].tolist()
    title_list3=df['信件组']
    # print(df2)
    # print(df2['变量'])
    """2。读取excel文件，返回list元组数据"""
    data_list=[]
    # zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    # 如果个个迭代器中的元素个数不一致，则返回列表长度与最短的对象相同，利用*操作符，可以激昂元组解压为列表
    # a=[1,2,3]
    # b=[4,5,6]
    # c=[4,5,6,7,8]
    # zipped=zip(a,b) # 结果是[(1,4),(2,5),(3,6)]
    for i,j,k in zip(title_list1,title_list2,title_list3):
        data_tup=(i,j,k)
        data_list.append(data_tup)
    print(data_list)
    return data_list
"""2.读取excel文件，返回list字典数据"""
def read_excel_to_dict():
    file='邮件模板.xlsx'
    df=pd.read_excel(file,sheet_name='主编信件',header=0,skiprows=2)
    title_list1=df['事件'].tolist()
    title_list2=df['模板ID'].tolist()
    title_list3=df['信件组']
    data_list=[]
    for i,j,k in zip(title_list1,title_list2,title_list3):
        data_dict={"title1":i,"title2":j,"title3":k}
        data_list.append(data_dict)
    print(data_list)
    return data_list
"""3.list保存excel文件"""
def save_excel():
    """
    pandas 数据类型DaTaFrame（数据框）：可以看成excel表，dataframe是一种表格类型数据结构，它含有一组有序的列，每列可以是不同
    的值类型（数值，字符串、布尔）。dataframe既有行索引也有列索引，行索引和列索引是标签
    dataframeLd 额创建有多种格式不过最重要的还是根据dict进行创建，以及读取csv或者txt文件创建
    :return:
    """
    df1=pd.DataFrame({"name":['tom','jone','marry'],
                      "age":[20,18,19],
                      "income":[1000,3000,2000],
                      "index":['person1','person2','person3']})
    # 精准修改列名（逐一修改列名）rename
    # 精准修改列名 df1.index=range(0,len(df1.index))
    # # df1.rename(index={'per'})
    df1.rename(columns={"name": "名字", "age": "年龄"}, inplace=True)
    # 增加一列
    df1['pay']=[20,30,40]
    #将增加的列设置修改到某一位置
    # df1.insert(0,'pay',df1.pop('pay'))
    # print(df1)
    # print(df1.index)# 行索引
    # print(df1.columns)# 列索引
    # print(df1.values)# 值

    data_df=pd.DataFrame()
    data_dict={}
    for i in range(100):
        data_dict['标题1']='我是内容{}'.format(i)
        data_df=data_df.append(data_dict,ignore_index=True)
    # 写文件的时候要注意 如果excel表格是打开的，那么数据流是写入不进去的
    # 如果excel表格中有多个sheet页，只有w 其他的sheet页数据也会被删除掉 只留下新的数据
    with pd.ExcelWriter('邮件模板.xlsx') as w:
        data_df.to_excel(w,encoding='utf-8',index=False,sheet_name='Sheet1')
    """csv文件处理"""
    # csv文件读取
    # dd=pd.read_csv("文件路径")
    """list转存成csv"""
    list=[[1,2,3],[4,5,6],[7,8,9]]
    name=['a','b','c']
    test=pd.DataFrame(columns=name,data=list)
    print(test)
    test.to_csv('data.csv',encoding='utf-8')
if __name__ == '__main__':
    # read01_excel_data()
    save_excel()