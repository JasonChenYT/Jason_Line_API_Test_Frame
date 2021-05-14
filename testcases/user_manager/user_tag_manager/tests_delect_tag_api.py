# @ending: utf-8  @author: JasonChen 
# @file: tests_delect_tag_api.py   @time = 2021/4/29 18:35
# @desc:
import unittest
import requests
import jsonpath
from common.log_utils import logger
from common import public_api_infos


class TestDelectTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        logger.info('---------删除用户标签用例开始执行-----------')

    def tearDown(self) -> None:
        self.session.close()
        logger.info('---------删除用户标签用例执行完毕-----------')

    def test_delect_tagsID_0(self):
        self._testMethodName = 'API_CASE_04'
        self._testMethodDoc = '验证不能删除tagsId为0的标签'
        logger.info('执行用例【%s】' % self._testMethodDoc)
        token_id = public_api_infos.get_access_token(self.session)
        logger.info('获取token成功')
        url_params = {"access_token": token_id}
        post_data ={"tag": {"id": 0}}
        response = public_api_infos.delect_user_tag_api(self.session, url_params, post_data)
        actual_result = jsonpath.jsonpath(response.json(), '$.errcode')[0]
        self.assertEqual(actual_result, 45058, 'API_CASE_04用例执行失败')


if __name__ == '__main__':
    unittest.main(verbosity=2)