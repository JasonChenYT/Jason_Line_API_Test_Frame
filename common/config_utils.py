# @ending: utf-8  @author: JasonChen 
# @file: config_utils.py   @time = 2021/3/17 16:38
# @desc:

# 方式一
# class ConfigUtils:
#     @property  # 属性方法  调用不需要打括号
#     def HOSTS(self):
#         return 'api.weixin.qq.com'
#
# config = ConfigUtils()
#
# if __name__ == '__main__':
#     print(config.HOSTS)  # HOSTS属性方法

# 方法二 配置文件读取
import configparser  # 导入内置包
import os

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', 'conf', 'config.ini')

class ConfigUtils:
    def __init__(self,config_file=config_path):
        self.cfg_obj = configparser.ConfigParser() # 创建一个配置文件对象
        self.cfg_obj.read(config_file, encoding='utf-8' )  # 把配置文件加载到配置文件对象中

    @property
    def HOSTS(self):
        hosts_value = self.cfg_obj.get('default', 'HOSTS')  # 使用get方法进行取值
        return hosts_value

    @property
    def CASE_PATH(self):
        case_path_value = self.cfg_obj.get('path','CASE_PATH')
        return case_path_value

    @property
    def APPID(self):
        appid = self.cfg_obj.get('userinfo', 'APPID')
        return appid

    @property
    def SECRET(self):
        secret = self.cfg_obj.get('userinfo', 'SECRET')
        return secret

    @property
    def SMTP_SERVER(self):
        smtp_server = self.cfg_obj.get('email','SMTP_SERVER')
        return smtp_server

    @property
    def SENDER(self):
        sender = self.cfg_obj.get('email','SENDER')
        return sender

    @property
    def PASSWORD(self):
        password = self.cfg_obj.get('email','PASSWORD')
        return password

    @property
    def RECEIVER(self):
        receiver = self.cfg_obj.get('email','RECEIVER')
        return receiver

    @property
    def CC(self):
        cc = self.cfg_obj.get('email','CC')
        return cc

    @property
    def SUBJECT(self):
        subject = self.cfg_obj.get('email','SUBJECT')
        return subject


config = ConfigUtils()

if __name__ == '__main__':
    print(config.SUBJECT)
    print(config.PASSWORD)
    print(config.SENDER)
    print(config.CC)
    print(config.RECEIVER)