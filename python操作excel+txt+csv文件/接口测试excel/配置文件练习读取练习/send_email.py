

"""smtp：全称是simple mail transfer protocol简称简单的额邮件传输协议，它是一组用于从源地址到目的地传输邮件的规范，通过它来控制邮件
的中转方式，smtp协议属于tcp/ip协议簇，它帮助每台计算机在发送或中转信件时找到下一个目的地
smtp：通信的基本流程可以概括为
1.链接smtp服务器
2。登陆用户名、密码
3。发送指定邮件内容
4。退出smtp链接
.join的特殊方法：
    基本公式：《需要在每个元素中间添加字符》.join(目标list，且所有的元素都为str类型)，返回一个新的字符串
    需要注意的是 一定是list集合 所有数据必须是str类型，其他类型则报错
"""
import smtplib # 加载smtplib模块
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 发送邮件相关参数
from email.utils import formataddr
from email.header import Header
'''邮箱账号的授权码：GWWJVBVVLBPSUNZX
用于邮件发送过程中需要传入的验证数据信息
'''
# 1。需要设置的基础信息内容
my_sender='18803836226@163.com' # 发件人邮箱账号
"""这个是单独的邮箱发送"""
# my_user='1045029810@qq.com' # 收件人邮箱账号，为了便于维护，所以写成了变量
my_user=["1045029810@qq.com","wangmm@ipublishment.cn"]
my_authorization_code='GWWJVBVVLBPSUNZX'
my_smtp='smtp.163.com' # 163的smtp服务
my_stmp_port=25 # 163的smtp服务端口号
dd={}
# dd['ff']=";".join(my_user)
# print(dd['ff'])
# exit()
def more_file():
    currentPath=os.getcwd()
    targetPath=os.path.join(currentPath,'data')
    sqlFileList=os.listdir(targetPath)
    sqlFilePath=''
    sqlFilePathList=[]
    for fileName in sqlFileList:
        sqlFilePath=os.path.join(targetPath,fileName)
        sqlFilePathList.append(sqlFilePath)
        """这种方法只能能适用于目录下的文件类型都是一样的"""
        # msg = MIMEMultipart()  # 多个部分的
        # with open(sqlFilePath, 'rb') as f:
        #     part = MIMEApplication(f.read())
        #     part.add_header('Content-Disposition', 'attachment', filename=fileName)
        #     msg.attach(part)
    return sqlFilePathList

def mail():
    ret=True
    try:
        """邮件模式一：发送纯文本格式的邮件"""
        msg=MIMEText("我是测试内容,我喜欢你 掉入了海底 啊啊啊啊啊 喜欢你",'plain','utf-8')
        # """邮件模式二：这个是邮件题"""
        # msg=MIMEMultipart()

        msg['From']=formataddr(['username',my_sender]) # 括号里面对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=';'.join(my_user)# 括号里面对应的是收件人邮箱昵称 收件人邮箱
        subject='梦梦做python smtp邮件测试'
        msg['Subject']=Header(subject,'utf-8')




        """发送邮件 创建smtp服务器 登陆服务器 发送邮件"""
        server=smtplib.SMTP(my_smtp,my_stmp_port)
        server.login(my_sender,my_authorization_code)
        server.sendmail(my_sender,my_user,msg.as_string())#括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭链接
    except Exception as e:
        print(e)
        ret=False
    return ret
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")