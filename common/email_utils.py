# @ending: utf-8  @author: JasonChen 
# @file: email_utils.py   @time = 2021/4/30 14:41
# @desc:邮件工具包
import email
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import config


class EmaiUtils:
    def __init__(self,email_body,email_attach_path=None):
        self.smtp_server = config.SMTP_SERVER
        self.sender = config.SENDER
        self.password = config.PASSWORD
        self.receiver = config.RECEIVER
        self.cc = config.CC
        self.subject = config.SUBJECT
        self.body = email_body
        self.attach_path = email_attach_path

    def email_body(self):  # 邮件主体
        email_obj = MIMEMultipart()
        email_obj['from'] = self.sender
        email_obj['to'] = self.receiver
        email_obj['Cc'] = self.cc
        email_obj['subject'] = self.subject
        email_obj.attach(MIMEText(self.body,'html','utf-8') )
        if self.attach_path:
            attach_file = MIMEText(open(self.attach_path, 'rb').read(), 'base64', 'utf-8')
            attach_file['Content-type'] = 'application/octet-stream'
            attach_file.add_header('Content-Disposition', 'attachment', filename=('gbk', '', os.path.basename(self.attach_path)))
            email_obj.attach(attach_file)
        return email_obj

    def send_email(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.sender,password=self.password)
        smtp.sendmail(self.sender,self.receiver.split(",")+self.cc.split(","),self.email_body().as_string())
        smtp.close()

if __name__=="__main__":
    email_body = '''
    <h3 align ="center">接口自动化测试报告</h3>
    <p align = "center">详情请查阅附件</p>
    '''
    current_path = os.path.dirname(__file__)
    html_file_path = os.path.join(current_path, '..', 'html_reports', 'WX_API_TESTV1.9', 'WX_API_TESTV1.9.html')
    EmaiUtils(email_body,html_file_path).send_email()

