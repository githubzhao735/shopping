from django.http import JsonResponse

from common import errors


def render_json(code=errors.OK,data=None):
    """
    返回json字符串
    :param code: 状态码
    :param data: 数据
    :return: json字符串
    """

    result = {
        "code":code
    }
    if data :
        result["data"] = data

    return JsonResponse(result,json_dumps_params={"separators":(",",":")})




