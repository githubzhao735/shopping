
from common.config import yunzhixin
import requests
from common.response_code import RET
from common.return_json import return_json


def send_sms(request,phone,sms_code):
    url= 'https://open.ucpaas.com/ol/sms/sendsms'
    params = yunzhixin.copy()

    params['mobile'] = phone
    params['param'] = sms_code

    # print(params)
    try:
        resp = requests.post(url=url, json=params)
        print(999999)
    except Exception as e:
        print(e)
        return return_json(RET.THIRDERR,'發送短信失敗')
    else:
        print(8888)
        print(resp)
        return resp
