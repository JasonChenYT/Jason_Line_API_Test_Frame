# @ending: utf-8  @author: JasonChen 
# @file: log_utils.py   @time = 2021/4/29 0:58
# @desc:日志文件工具包
import os
import time
import logging

current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path, '../logs')


class LogUtils:
    def __init__(self, log_path=log_output_path):
        self.log_file_path = os.path.join(log_path, 'WX_API_%s'%time.strftime('%Y-%m-%d'))
        self.__logger = logging.getLogger('WX_API_TEST')
        self.__logger.setLevel(logging.DEBUG)   # 10

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_file_path, 'a', encoding='utf-8')
        formatter = logging.Formatter("jason:%(asctime)s__%(name)s__%(levelname)s__%(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.__logger.addHandler(console_handler)
        self.__logger.addHandler(file_handler)

        console_handler.close() # 防止日志打印重复 可以解决一半
        file_handler.close()

    def get_logger(self):
        return self.__logger


logger = LogUtils().get_logger() # 调用时建议使用一个对象进行打印日志，，否则容易出现日志重复。

if __name__ == '__main__':
    logger.info('接口用例开始....')
    logger.debug('接口用例调试使用')
    logger.error('服务未启动，404~')
    logger.warning('未识别搭配文件file')
    logger.critical('系统崩溃了。505~')
