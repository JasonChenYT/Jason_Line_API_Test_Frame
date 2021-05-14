# @ending: utf-8  @author: JasonChen 
# @file: run_all_testcase.py   @time = 2021/3/14 14:26
# @desc:
import unittest
import os
import sys
import shutil
from common import HTMLTestReportCN
from common.log_utils import logger
from common.email_utils import EmaiUtils


logger.info('============WX_API_TEST_接口测试开始执行===============')
crrent_path = os.path.dirname(__file__)
case_path = os.path.join(crrent_path, 'testcases')
html_report_path = os.path.join(crrent_path, 'html_reports/')
discover_cases = None # 为空
try:
    discover_cases = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                     pattern='tests*.py')
except ImportError as e:
    logger.error('测试用例路径出错，导致不能加载测试用例')
except Exception as e:
    logger.error('系统出错，错误原因:%s'%e.__str__())
api_case_suite = unittest.TestSuite()
if discover_cases:  # 加载到数据执行如下语句块
    api_case_suite.addTest(discover_cases)
    logger.info('加载测试用例到测试套件成功')
else:  # 否则执行如下语句块
    logger.error('加载测试用例到测试套件失败')

html_report_path_obj = HTMLTestReportCN.ReportDirectory(html_report_path)
html_report_path_obj.create_dir('WX_API_TEST')  # 创建测试报告路径
# 创建测试报告网页文件路径
html_report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_report_file_obj = open(html_report_file_path,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=html_report_file_obj,
                                         tester='jasonchen',
                                         title='微信公众号平台接口测试项目',
                                         description='实战使用')
runner.run(api_case_suite)
logger.info('===============WX_API_TEST_接口测试执行完毕=================')

email_body = '''
    <h3 align ="center">接口自动化测试报告</h3>
    <p align = "center">详情请查阅附件</p>
    '''
# EmaiUtils(email_body,html_report_file_path).send_email()  # 邮件发送
# 强制复制不提醒
shutil.copyfile(html_report_file_path, '%s/WX_API_TESTV.html'% sys.argv[1])  # 拷贝文件，sys.argv可以传入参数

