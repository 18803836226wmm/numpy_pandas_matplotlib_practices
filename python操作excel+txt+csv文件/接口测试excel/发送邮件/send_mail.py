import os
import smtplib
import time

import schedule

import read_config
import getPathInfo
from email.mime.text import MIMEText # 发送正文
from email.mime.multipart import MIMEMultipart #发送多个部分
from email.mime.application import MIMEApplication # 发送附件
from email.header import Header # 从email包引入header方法 用来构建邮件头

read_conf=read_config.ReadConfig()
mail_host=read_conf.get_email('mail_host') #从配置文件中读取host
mail_sender=read_conf.get_email('mail_sender')# 从配置文件中读取
mail_authorization_code=read_conf.get_email('authorization_code') # 配置文件读取授权码
subject=read_conf.get_email('subject')
mail_receivers=read_conf.get_email('mail_receivers')
# 获取测试报告的路径
mail_path=os.path.join(getPathInfo.get_path(),'result','report.html')
print(mail_path)
class TestMail(object):
    def send_mail(self):
        msg=MIMEMultipart()#邮件体
        msg['From']=mail_sender
        msg['To']=mail_receivers
        #获取系统时间
        tm=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        #邮件主题
        msg['Subject']=Header(subject+'_'+tm,'utf-8')
        conten="我是邮件正文"
        email_body=MIMEText(conten,'plain','utf-8')
        msg.attach(email_body)# 将正文添加到邮件体中
        #构建附件
        att=MIMEApplication(open(mail_path,'rb').read())#打开附件
        att.add_header("Content-Disposition", "attachment", filename='测试报告.html')
        msg.attach(att)
        try:
            server = smtplib.SMTP(mail_host, 25)
            server.login(mail_sender, mail_authorization_code)
            server.sendmail(mail_sender, mail_receivers, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭链接
            print("邮件发送成功")
        except Exception as e:
            print("邮件发送失败")
            print(e)
mail_job=TestMail()
def job():
    print("开始工作了")
    schedule.every(10).seconds.do(mail_job.send_mail)
job()
while True:
    schedule.run_pending()
    time.sleep(1)