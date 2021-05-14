# @ending: utf-8  @author: JasonChen 
# @file: log.py   @time = 2021/4/29 17:59
# @desc:
'''
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息
'''
import logging


logger = logging.getLogger('jasonLogWork')
logger.setLevel(10)

handler1 = logging.StreamHandler()
formatter = logging.Formatter('%(levelno)s_%(levelname)s_%(pathname)s_%(filename)s_%(funcName)s_%(lineno)d_%(asctime)s_%(thread)d_%(threadName)s_%(process)d_%(message)s')

handler1.setFormatter(formatter)
logger.addHandler(handler1)

logger.info('hi Qiucy,this is your pragram')