from common.response_code import RET
import re
from common.request_method import check_request_method
from common.return_json import return_json
from user.logics import gen_sms_code
from utils.yunzhixun import send_sms
from django.core.cache import cache
from common.constants import VERIFY_CODE

@check_request_method('POST')
def verify_phone_num(request):
    """
    驗證手機號格式
    :param request:
    :return:
    """
    phone = request.POST.get('phone')

    #校驗數據
    if not all([phone]):
        # return JsonResponse({'code':RET.NODATA,'msg':'手機不能爲空'})
        return return_json(RET.NODATA,'手機不能爲空')

    if not re.match(r'^1[3-9]\d{9}$',phone):
        return return_json(RET.DATAERR,'手機格式錯誤')

    #生成驗證碼
    sms_code = gen_sms_code(phone)
    print(sms_code,type(sms_code))

    #爲了不用每次都發送短信，生成驗證碼後設置爲緩存
    cache.set(VERIFY_CODE.format(phone),sms_code,60*5)

    #發送驗證碼
    # resp = send_sms(request,phone,sms_code)
    # print(resp,type(resp))
    #
    # if resp.status_code == 200:
    #
    #     ret = resp.json()
    #     print(ret,type(ret))
    #     if ret.get('code') == '000000':
    #         return return_json(RET.OK,'OK')
    #
    # return return_json(RET.THIRDERR,'第三方系统错误')
    return return_json(RET.OK,'ok')






