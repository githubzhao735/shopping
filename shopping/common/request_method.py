from django.http import JsonResponse
from .response_code import RET
from common.return_json import return_json

def check_request_method(method):
    def outter(func):
        def inner(request,*args,**kwargs):
            if request.method != method:
                  return  return_json(RET.REQUESTMETHODERR,'請求方式錯誤')
            return func(request,*args,**kwargs)
        return inner
    return outter

