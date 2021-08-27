# 方式一 为对象初始化自己独有的特征
class people(object):
    country='china'
    x=1
    def run(self):
        print('-----',self)
# 实力话出3个对象
obj1=people()
obj2=people()
obj3=people()
# 为对象定制自己特有的特征
def chu_shi_hua(obj,x,y,z):
    obj.name=x
    obj.age=y
    obj.sex=z
    print(obj.name,obj.age,obj.sex)
chu_shi_hua(obj1,"1",12,"nvde")
chu_shi_hua(obj3,"2",33,"nan")



