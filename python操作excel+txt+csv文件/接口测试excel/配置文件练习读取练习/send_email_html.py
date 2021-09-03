from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib,os,time,schedule


my_sender='18803836226@163.com' # 发件人邮箱账号
"""这个是单独的邮箱发送"""
# my_user='1045029810@qq.com' # 收件人邮箱账号，为了便于维护，所以写成了变量
my_user=["1045029810@qq.com","wangmm@ipublishment.cn","18803836226@163.com"]
my_authorization_code='GWWJVBVVLBPSUNZX'
my_smtp='smtp.163.com' # 163的smtp服务
my_stmp_port=25 # 163的smtp服务端口号

def get_report(report_path):
    """获取最新的测试报告"""
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(report_path, lists[-1])
    #    L=file_path.split('\\')
    #    file_path='\\\\'.join(L)
    return file_path
def send_mail():
    # 发送html格式的邮件
    htmlfile=MIMEText('<html><body><a href="">百度一下</a></p></body></html>','html','utf-8')
    """构造一个邮件体：包含正文、附件"""
    msg=MIMEMultipart()# 邮件体
    msg['From']=my_sender
    msg['To']=';'.join(my_user)
    tm=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))#获取系统时间
    msg['Subject']=Header('接口测试邮件报告'+tm,'utf-8')
    #构建正文内容信息
    content="""执行测试中。。。。
                测试已完成
                生成报告中
                报告已生成
                报告已经邮件发送"""
    email_body=MIMEText(content,'plain','utf-8')
    msg.attach(email_body)# 将正文添加到邮件体中
    # 构建附件 打开附件
    att=MIMEApplication(open('/python操作excel+txt+csv文件/接口测试excel/配置文件练习读取练习/data/index.html', 'rb').read())
    # 为附件命名
    att.add_header("Content-Disposition", "attachment",filename='王梦测试报告.html')
    msg.attach(att)
    try:
        server = smtplib.SMTP(my_smtp, my_stmp_port)
        server.login(my_sender, my_authorization_code)
        server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭链接
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败")
        print(e)

def job():
    print("开始工作了")
    schedule.every(10).seconds.do(send_mail)
job()
while True:
    schedule.run_pending()
    time.sleep(1)
