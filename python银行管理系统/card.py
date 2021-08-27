class Card(object):
    def __init__(self,cardStr,cardPwd,cardMoney):
        # 定义卡类并初始化卡的基本信息
        self.cardStr=cardStr
        self.cardPwd=cardPwd
        self.cardMoney=cardMoney
        # 卡号是否被锁
        self.isLock=False