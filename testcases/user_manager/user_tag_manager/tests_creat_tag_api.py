# @ending: utf-8  @author: JasonChen 
# @file: tests_creat_tag_api.py   @time = 2021/3/14 15:18
# @desc:
import requests
import unittest
import jsonpath
import json
from common.config_utils import config
from common import public_api_infos
from common.log_utils import logger

class TestGetAccessToken(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS  # 方式一
        self.session = requests.session()
        logger.info('---------用户管理开始执行-----------')

    def tearDown(self) -> None:
        self.session.close()
        logger.info('---------用户管理执行完毕-----------')

    def test_01_get_access_token(self):
        self._testMethodName = 'API_CASE_03'
        self._testMethodDoc = '测试正常进行创建标签接口调用'
        logger.info('正在执行【%s】' % self._testMethodDoc)
        token_id = public_api_infos.get_access_token(self.session)
        url_params = {"access_token": token_id}
        tag_info = {"tag": {"name": "贵州贵阳09"}}
        response = public_api_infos.create_user_tag_api(self.session, url_params, tag_info)
        actual_result = jsonpath.jsonpath(response.json(), '$.tag.name')[0]
        self.assertEqual(actual_result, '贵州贵阳09')


if __name__ == '__main__':
    unittest.main(verbosity=2)

