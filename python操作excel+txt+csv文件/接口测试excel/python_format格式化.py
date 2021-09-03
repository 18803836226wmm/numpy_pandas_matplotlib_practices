"""python .format函数的作用
    1关键字
    2位置
    3精度
    4进制转化
    5千万位分割符
2。对比%s、%d占位符号，这样格式的数据只能接受固定格式的数据，需要对接受的数据进行处理 .format可以接受任意格式的数据
3。python中join函数的使用方法
join():链接字符串数组。将字符串、元组、类标中的元素以指定（分割符） 链接成一个新的字符串
od.path.join():将多个路径组合后返回，且是自动携带路径的符号\。不需要手动再去添加
4.  字符串大小写转换
    字符串搜索相关 str.find(str,beg=0,end=len(string)) 检测字符串中是否包含字符串str 如果指定开始和结束范围
    则检查的范围是指定的beg和end结束范围
    """
#关键字
print("{name}在{option}".format(name='李白',option='玩'))
# 位置
print("name={} path={}".format('王梦梦','logon'))
print('{1}{0}'.format('梦梦','王'))
#填充和对齐^<> 分别表示居中、左对齐、右对齐 对齐的时候一定要加上冒号 格式才不会报错
print("{:>10}".format('haha'))
# 3精度
print('{:.3f}'.format(3.1415926))
# 千位分割符
print('{:,}'.format(10000000000))

seq1=['hello','good','boy','doiido']
str='Hello my name is hanmeimei'
print(str.upper())
print(str.swapcase())
print(str.capitalize())
print(str.title())
print(str.find('o')) #返回的是当前搜索的元素位置索引
print(type(str.find('o')))
print(str.find('m',2,len(str)))
print(str.index('m')) #查找同上面的方法一样 但是找不到结果会报错
print(str.count('m')) # 统计指定字符串出现的次数
print(str.rfind('l')) # 从右边开始查找
print(str.replace('m','k',1))# 分别代表被替换的字符、替换的字符 替换次数
exit()

print(';'.join(seq1))
print(type(';'.join(seq1)))
