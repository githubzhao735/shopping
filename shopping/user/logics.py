import random


def gen_sms_code(request):
    """
    生成隨機驗證碼
    :param request:
    :return:
    """
    sms_code = random.randrange(1000 ,10000)

    return str(sms_code)



