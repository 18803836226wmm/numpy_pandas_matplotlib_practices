import numpy as np
"""
numpy 常用方法
ndim：返回int 表示ndarray的维度
shape：返回的尺寸 几行几列
size：返回数组元素的个数
dtype：返回数组中元素的类型
运算 直接可以在每个元素加减乘除
"""
# arry0=np.array([1,2.3,2,3],dtype='int')
# print(arry0)
# x=np.linspace(1,5,5,endpoint=False)
# print(x)
# x2=np.zeros(3,int)+2
# print(x2)
# arr1=np.arange(1,7).reshape(3,2)
# arr2=np.arange(11,17).reshape(3,2)
#
# print(arr1)
# print(type(arr1))
# print(arr2)
#
# print(np.hstack((arr1,arr2))) # 横向拼接
# print(np.vstack((arr1,arr2))) # 纵向拼接
#
# print(np.concatenate((arr1,arr2),axis=1))
# print(np.concatenate((arr1,arr2),axis=0))

data=((8.5,6,4.1,2,0.7),(1.5,3,5.4,7.3,9),(3.2,4.5,6,3,9),(11.2,13.4,15.6,17.8,19))
print(data)
array2=np.array(data)
# print(array2)
# print(array2[0:1])
print(array2[1:3,0:1])
"""数据排序"""
data2=[4,2,2,1,9,4,6,8,7,9]
s=np.array(data2)
print(np.sort(s))
print(np.argsort(s))
# 降序排列 sorted
d=sorted(data2,reverse=True)
print(d)
arr1 = np.array([[0,1,3],[4,2,9],[4,5,9],[1,-3,4]])
print(arr1)
# axis 代表沿着的方向，0代表是行的方向，1代表是列的方向，不加axis参数默认按照1的方式排序
f=np.sort(arr1)
print(f)
u = np.array([1,2,3,4,3,1,2,2,4,6,7,2,4,8,4,5])
print(sorted(u))
j=np.argsort(u)
print(j)
"""数据搜索 np.where() 可以自定义返回满足条件的情况
np.extract:返回满足条件的元素值"""
g=np.where(u>3,1,-1)
print(g)
l=np.extract(s>3,s)
print(l)

t=np.arange(24).reshape(4,6)
print(t)
print(t[[1,2]])

