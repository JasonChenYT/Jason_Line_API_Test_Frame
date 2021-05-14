# @ending: utf-8  @author: JasonChen 
# @file: email_demo.py   @time = 2021/4/30 10:05
# @desc:
import email
import os
import smtplib
from email.mime.text import MIMEText

email_body = '''
<h1 align ="center">接口自动化测试报告</h1>
<p align = "center">详情请查阅附件</p>
'''
html_file_path = os.path.join(os.path.dirname(__file__),)


# 只用于界面显示，不会执行发送请求
email_obj = MIMEText(email_body, 'html', 'utf-8')
email_obj['from'] = '191695813@qq.com'  # 发件人 和登录名一致
email_obj['to'] = 'jasonchen@chen.com'  # 收件人
email_obj['Cc'] = 'Qiucy@chen.com'  # 抄送人
email_obj['subject'] = 'Qiucy接口自动化报告'

# 真的发送邮件请求
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
# 邮箱的授权码
smtp.login(user='191695813@qq.com', password='sdipksilkhdlcage')
smtp.sendmail("191695813@qq.com", "191695813@qq.com", email_obj.as_string())
smtp.sendmail("191695813@qq.com", ["191695813@qq.com","1984539808@qq.com"], email_obj.as_string())
smtp.close()



