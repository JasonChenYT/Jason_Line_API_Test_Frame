# @ending: utf-8  @author: JasonChen 
# @file: logs_demo.py   @time = 2021/3/17 20:34
# @desc:
import logging


# 相当于输出语句，默认输出error级别 ， info是不能输出的
# logging.info('info!da')
# logging.error('error!@##')

log_obj = logging.getLogger('jason')
log_obj.setLevel(10) # 需要设置默认的日志级别，下面的handler设置才生效。 总开发，一般默认设置小级别

handler1 = logging.StreamHandler()  # 创建handler对象 输出在控制台
handler1.setLevel(40)  # 利用handler设置日志等级

handler2 = logging.FileHandler('./test.log', 'a', encoding='utf-8') # 创建handler对象2  日志输出在指定的文件中
handler2.setLevel(30)
# 创建一个日志格式对象
formatter = logging.Formatter("jason:%(asctime)s__%(name)s__%(levelname)s__%(message)s")
# 把日志格式对象配置到handler对象
handler1.setFormatter(formatter)
formatter1 = logging.Formatter("Qiucy:%(asctime)s__%(name)s__%(message)s")
handler2.setFormatter(formatter1)
# 把handler对象设置加载到日志对象
log_obj.addHandler(handler1)
log_obj.addHandler(handler2)

log_obj.debug('debug')
log_obj.warning('warning')
log_obj.error('error')
log_obj.info('info级别')
log_obj.critical('critical')