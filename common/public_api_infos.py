# @ending: utf-8  @author: JasonChen 
# @file: public_api_infos.py   @time = 2021/3/17 19:28
# @desc:
import json
import jsonpath
from common.config_utils import config
from common.log_utils import logger
from requests.exceptions import RequestException


# 获取token
def get_access_token_api(session, url_params):
    logger.info('执行调用【get_access_token_api】开始')
    try:
        response = session.get(url='https://%s/cgi-bin/token' % config.HOSTS,
                                    params=url_params)  # params 参数的值就可以试字典类型的url参数
    except RequestException as e:
        logger.error('请求出现异常，错误原因：%s'%e.__str__())
    finally:
        logger.info('执行调用【get_access_token_api】结算')
    return response

def get_access_token(session):
    url_params = {
        "grant_type": "client_credential",
        "appid": config.APPID,
        "secret": config.SECRET
    }
    response = get_access_token_api(session, url_params)
    token_id = jsonpath.jsonpath(response.json(), '$.access_token')[0]
    return token_id


def create_user_tag_api(session, url_params, post_data ):
    tag_info_str = json.dumps(post_data, ensure_ascii=False)
    response = session.post(url='https://%s/cgi-bin/tags/create' % config.HOSTS,
                                 params=url_params,
                                 data=tag_info_str.encode('utf-8'))
    return response


def delect_user_tag_api(session, url_params, post_data):
    response = session.post(url='https://%s/cgi-bin/tags/delete' % config.HOSTS,
                            params=url_params,
                            json=post_data)
    return response