import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(): 
    # 第三方 SMTP 服务
    mail_host="smtp.exmail.qq.com"  #设置服务器
    mail_user="admin@emx6.com"    #用户名
    mail_pass="1qazXSW2"   #口令 
    
    
    sender = 'admin@emx6.com'
    receivers = ['2212280169@qq.com']  # 接收邮箱

    mail_msg='''
    每日一报提交失败,请前往github查看执行日志，以及别忘记手动填报上哈。 
    from 上帝不会掷骰子
    '''

    
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("余生", 'utf-8')
    message['To'] =  Header("Loie", 'utf-8')
    
    subject = '每日一报提交失败...'
    message['Subject'] = Header(subject, 'utf-8')
    
    
    try:
        smtpObj = smtplib.SMTP_SSL(host=mail_host) 
        smtpObj.connect(mail_host, 465)    # 465 为 SMTP 端口号
        
        smtpObj.login(mail_user,mail_pass)

        smtpObj.sendmail(sender, receivers, message.as_string())
        
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")