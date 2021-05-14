# @ending: utf-8  @author: JasonChen 
# @file: config_read_demo.py   @time = 2021/3/17 17:06
# @desc:
import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', 'conf', 'config.ini')

cfg_obj = configparser.ConfigParser()
cfg_obj.read(config_path,encoding='utf-8')
value = cfg_obj.get('default', 'HOSTS')
print(value)