"""
业务相关配置
"""

# 云之讯短信平台配置
# YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/{function}'

# YZX_SMS_PARAMS = {
#     'sid': '90c9485450dac51d3f00f8772eeffd49',
#     'token': 'c90bcd499306fa943d47079943c45327',
#     'appid': '25e548d8c5fb4964b5f6d618dccbbca8',
#     'templateid': '485707',
#     'param': None,
#     'mobile': None,
# }

YZX_SMS_URL =  'https://open.ucpaas.com/ol/sms/sendsms'

YZX_SMS_PARAMS ={

    "sid": "2dfc9d5d65b9024bfa50b12f40161ca9",
    "token": "199bbc3f31a4af02b1d37ad6b78dc917",
    "appid": "7723625e9eed46dd87b911c9cd21f1f7",
    "templateid": "485727",
    "param": None,
    "mobile": None
}

#七牛云存储平台配置
QINNIU_ACCESS_KEY = "9M_4LVjxHubwJP2yaT_uJTyeWJl-f9ct7zo3hVIG"
QINNIU_SECRET_KEY = "KmfZX-JrW-Bj36R-5fjHAK_7AOTzTqnfsKFC1HMn"
QINNIU_BUCKET_NAME = "shopping"
QINNIU_HOST = "http://putktasgp.bkt.clouddn.com/"




