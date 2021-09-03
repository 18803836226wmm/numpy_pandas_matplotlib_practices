"""
这个是atm各种操作的类
"""
import random
import time
import pickle
from python银行管理系统.card import Card
from python银行管理系统.user import User
class ATM(object):
    # 初始化
    def __init__(self,alluserInfo):
        # 初始化所有的用户信息，以便于以后操作以及校验 包括卡号、用户
        self.alluserInfo=alluserInfo
    # 确认密码
    def checkPwd(self,realPwd):
        myList=[3,2,1,0]
        for i in myList:
            #银行系统中的判断 当数据为0的时候
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
            # if not self.alluserInfo.get(str):
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
            print(cardStr)
            # print(card.cardStr,card.cardPwd,card.cardMoney)
            print(user.name,user.idCard,user.phone,(card.cardStr,card.cardPwd,card.cardMoney))
            # 按卡号 ：用户信息 键值对的形式存入字典中
            self.alluserInfo[cardStr]=user

            print(self.alluserInfo)
            # 提示用户已经开户成功
            time.sleep(1)
            print("请牢记卡号{}".format(cardStr))
        except Exception as e:
            print(e)
            print("抱歉出现故障，暂时无法操作")
            return
    # 判断卡号是否存在
    def isExistence(self,cardStrInp):
        #卡号不存在，直接退回到选项页面
        if self.alluserInfo.get(cardStrInp):
            return True
        # 卡号不存在的情况下
        else:
            print("卡号不存在")
        return False
        print("账号咩有存在咩")
    # 做查询等操作时，输入密码
    def secretOption(self,cardStrinp):
        mylist=[3,2,1,0]
        for i in mylist:
            #如果密码输入错误超过三次
            if i==0:
                return False
        passInp=input("请输入密码")
        if passInp==self.alluserInfo[cardStrinp].cardInfo.cardPwd:
            return True
        elif (i-1)!=0:
            print("输入错误，你还有%d次输入机会"%(i-1))
    # 查询用户信息
    def searchUserInfo(self):
        # 用户想查询的卡号
        cardStrInfo=input("请输入卡号")
        # 判断卡号的状态
        isExist=self.isExistence(cardStrInfo)
        # 卡号存在
        #     if isExist:
        #         # 是否被锁定
        #         if not self.alluserInfo[cardStrInfo].cardInfo.isLock:
        #             # 输入密码并判断
        #             # 密码正确则输出余额
        #             if self.secretOption(cardStrInfo):
        #
        #      return -1
if __name__ == '__main__':
    file=open('database.txt','rb')
    allUserInfo = pickle.load(file)
    file.close()
    print(allUserInfo)







