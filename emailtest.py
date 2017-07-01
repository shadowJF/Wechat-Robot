import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'liangjfc@yonyou.com'  
receiver = ['liangjfc@yonyou.com','shipl@yonyou.com']  
subject = 'python email test'  
username = 'liangjfc'  
password = 'woaiwojia9'  
  
msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('mail.yonyou.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  
