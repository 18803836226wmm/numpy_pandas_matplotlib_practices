"""
这个是atm各种操作的类
"""
import random
import time
from python银行管理系统.card import Card
from python银行管理系统.user import User
class ATM(object):
    # 初始化
    def __init__(self,alluserInfo):
        # 初始化所有的用户信息，以便于以后操作 包括卡号、用户
        self.alluserInfo=alluserInfo
    # 确认密码
    def checkPwd(self,realPwd):
        myList=[3,2,1,0]
        for i in myList:
            if i==0:
                return False
        rePass=input("请再次输入密码")
        if realPwd==rePass:
            return True
        elif (i-1)!=0:
            print("输入错误，你还有%d机会"%(i-1))
    #随机生成开户卡号
    def randomId(self):
        while True:
            # 存放卡号
            str=''
            #随机生成6位卡号
            for i in range(6):
                #chr用在一个范围内在（0，255）整数作参数，返回一个对应的字符
                # ord 是chr函数的配对函数，它以一个字符串作为参数，返回值是对应的十进制整数
                ch=chr(random.randrange(ord('0'),ord('9')+1))
                str+=ch
            # 判断卡号是否重复 根据卡号能不能获取到值
            if not self.alluserInfo.get(str):
                return str
    # 这个是开卡操作
    def createUser(self):
        try:
            name=input("请输入姓名")
            idCard=input("请输入身份证号")
            phone=input("请输入手机号")
            preMoney=int(input("请输入存入的金额"))
            if preMoney<0:
                print("开卡失败")
                return -1
            # 设置密码
            onePwd=input("请输入密码")
            twoPwd=self.checkPwd(onePwd)
            if not twoPwd:
                print("确认密码错误，开户失败")
                return -1
            # 以上全部信息完成，则开户所需要的信息准备齐全，开户成功
            # 系统生成开户卡号
            cardStr=self.randomId()
            # 创建一个卡的实例，用于存储卡的信息
            card=Card(cardStr,onePwd,preMoney)
            # 创建一个用户信息用于存储用户
            user=User(name,idCard,phone,card)
            # 按卡号 用户信息 键值对的形式存入字典中
            self.alluserInfo[cardStr]=user
            # 提示用户已经开户成功
            time.sleep(1)
            print("请牢记卡号{}".format(cardStr))
        except:
            print("抱歉出现故障，暂时无法操作")
            return
    # 判断卡号是否存在
    def isExistence(self):
        print("账号咩有存在咩")
        pass


