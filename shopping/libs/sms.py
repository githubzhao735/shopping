from django.core.cache import cache

from common.utils import *
import requests
from common import config, cache_config


def send_verify_code(phone_num):
    """
    发送验证码
    :return: 第三方接口云之讯的json字符串
    """
    code = get_random_code(6)
    # print(code)

    data = config.YZX_SMS_PARAMS.copy()

    data["param"] = code
    data["mobile"] = phone_num

    cache.set(cache_config.VERIFY_CODE_PREFIX.format(phone_num), code, 24*60*60)

    resp = requests.post(config.YZX_SMS_URL, json = data)
    if resp.status_code == 200:

        ret = resp.json()

        if ret.get("code")=='000000':


            cache.set(cache_config.VERIFY_CODE_PREFIX.format(phone_num),code,3*60)

            return True

    else:

        return False





