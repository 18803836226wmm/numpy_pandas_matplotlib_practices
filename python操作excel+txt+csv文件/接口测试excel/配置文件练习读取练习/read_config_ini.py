import configparser



# 实例化configparaser对象
config=configparser.ConfigParser()
#read 读取ini文件
config.read("./data/config.ini")
#获取到所有的section 并以列表的形式返回
print(config.sections())
# 获取到所有的options
print(config.options('config'))
# iterms(section) 得到该section的所有键值对
print(config.items('cmd'))
# -get(section,option) 得到section中option的值，返回为string类型
print(config.get('cmd','viewphone'))
# getint(section,option) 得到section中的值 返回为int类型
# print(config.getint('cmd','id'))
"""写入配置文件"""
list=[]
list=config.sections()#获取配置文件中所有分组名称
if 'wwww' not in list:# 如果分组type 不存在则插入type组
    config.add_section('wwww')
    config.set('wwww','wmm','2222')
config['url']={'url':'www.baidu.com'} #类似与字典操作
o=open('./data/config.ini','w')
config.write(o)
o.close()
