from django.http import JsonResponse


def return_json(code,msg,data=None):
    """
    格式化返回的信息
    :param code:
    :param msg:
    :param data:
    :return:
    """

    result = {
        'code': code,
        'msg':msg,
    }

    if data:
        result['data'] = data

    json_dumps_params = {
        'separators': (',', ':')
    }

    return JsonResponse(data=result, json_dumps_params=json_dumps_params)