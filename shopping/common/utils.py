import random
import re


def is_phone_num(phone_num):
    """
    验证手机号码格式
    :param phone_num: 手机号码
    :return: True or False
    """
    pattern = re.compile(r"^1[3-9]\d{9}$")

    if pattern.match(phone_num.strip()):
        return True
    else:
        return False


def get_random_code(length=4):
    """
    生成验证码
    :param length: 验证码长度
    :return: 生成的验证码
    """
    if not isinstance(length,int):
        length = 1
    if length < 0 or length == 0:
        length = 1

    code = random.randrange(10**(length-1),10**length)

    return str(code)



