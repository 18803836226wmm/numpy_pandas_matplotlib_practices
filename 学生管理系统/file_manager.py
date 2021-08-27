"""
分析：学生管理系统应该包含老师注册登录、学生的增删改查 还有数据的持久化
因为数据存入json文件，所以需要读取和修改文件
密码加密可以用到哈希块文件
老师和学生的类文件
程序入口
核心增删改查文件
核心思想 采用面向对象的方式来学习
"""
import json
base_dir='/Users/wangmengmeng/numpy_pandas_matplotlib_practices/学生管理系统/data/' #定义一个变量 文件路径
#读取文件的函数
def read_file(file_name):
    # print(base_dir + file_name)
    try:
        with open(base_dir+file_name,'r',encoding='utf-8') as file:
            content=file.read()
            return content
    except FileNotFoundError:
        print("文件未找到")
def write_file(file_name,data):
    with open(base_dir+file_name,'w',encoding='utf-8') as file:
        # print(base_dir+file_name)
        file.write(data)
def write_json(file_name,data):
    with open(base_dir+file_name,'w',encoding='utf-8') as file:
        json.dump(data,file)
def read_json(file_name,default_data):
    try:
        with open(base_dir+file_name,'r',encoding='utf-8') as file:
            return json.load(file)
            #这个地方不能直接写成 json.load(file)，需要对文件做一下判断。因为open函数返回的是一个可迭代对象
            #迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置对象。迭代器对象是从集合的第一个元素开始访问，直到所有的元素被访问结束
            # 迭代器只能往前不会后退
            #不会后退是关键，也就是函数中，用load_f.read读取了可迭代对象后，file.read()文件的内容就读入了内存，file中没有字符，所以就读取 不到任何内容
            # if len(file.read())>0:
            #     datas=json.load(file)
            # else:
            #     datas={}
        #     if len(file.read())>0:
        #         datas=json.load(file)
        #     else:
        #         datas=default_data
        # return datas
    except FileNotFoundError:
        print('文件不存在')

if __name__ == '__main__':
   # d= read_json('data.json',{})
   # print(d)
   jj='333'
   write_file('students.txt',jj)

