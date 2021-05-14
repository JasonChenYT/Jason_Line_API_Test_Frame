# @ending: utf-8  @author: JasonChen 
# @file: tests_get_access_token_api.py   @time = 2021/3/14 14:28
# @desc:
import requests
import unittest
import jsonpath
from common.config_utils import config
from common import public_api_infos
from common.log_utils import logger

class TestGetAccessToken(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()
        logger.info('==========开始开发开始执行============')

    def tearDown(self) -> None:
        self.session.close()
        logger.info('==========开始开发执行完毕============')

    def test_01_get_access_token(self):
        logger.info('------------------------------------------')
        logger.info('-----执行第一条测试用例【获取access_token】----')
        try:
            url_params = {
                "grant_type": "client_credential",
                "appid": "wx70e792e1147fa788",
                "secret": "f44e3b57ff66ca6d632ee646974024c8"
            }
            response = public_api_infos.get_access_token_api(self.session, url_params)
            json_body = response.json()
            actual_result = jsonpath.jsonpath(json_body,'$.access_token')[0]
            logger.info('获取token成功【%s】' % actual_result)
            self.assertTrue(actual_result)  # 断言是否存在
        except AssertionError as e:
            logger.info('用例【获取access_token】断言失败')
        except Exception as e:
            logger.error('%s'%e.__str__())
        finally:
            logger.info('---执行第一条测试用例【获取access_token】结束---')
            logger.info('------------------------------------------')


    def test_02_grant_type_none(self):
        self._testMethodName = 'API_CASE_02'
        self._testMethodDoc = '验证grant_type参数为空时是否能正常获取access_token'
        logger.info('执行第二条用例【%s】' % self._testMethodDoc)
        url_patams = {
            "grant_type": "",
            "appid": "wx70e792e1147fa788",
            "secret": "f44e3b57ff66ca6d632ee646974024c8"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'% self.hosts,
                                params=url_patams)  # params 参数的值就可以试字典类型的url参数

        json_body = response.json()
        actual_result = jsonpath.jsonpath(json_body,'$.errcode')[0]
        self.assertEqual(actual_result, 40002)  # 断言是否存在



if __name__ == '__main__':
    unittest.main(verbosity=2)

