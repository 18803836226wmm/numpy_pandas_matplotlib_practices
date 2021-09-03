from faker import Faker


class HandlePhone(object):
    def __init__(self):
        self.fk=Faker(locale='zh-cn')
    # 对系统手机号前缀要求
    def __faker_phone(self):
        phone=self.fk.phone_number()
        print("生成的手机号",phone)
        return phone
    # 获取数据库的查询结果
    def __select_phone(self):
        sql=''
        # 接下来就是数据库查询的数据查询执行
        return
    # 获取未注册的手机号
    def get_phone(self):
        while True:
            phone=self.__faker_phone()
            result=self.__select_phone(phone)#将获取到的phone去数据库执行 查看执行结果，查看数据库中是否存在
            if len(result)>0:
                continue
            else:
                return phone
