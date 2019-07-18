from django.utils.deprecation import MiddlewareMixin
from common.response_code import RET
from common.return_json import return_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        自定义认证中间件

        白名单

        request.path

        根据 request.session['uid'] 来判断登录状态

        :param request:
        :return:
        """
        # WHITE_LIST = [
        #     '/api/verify_phone/',
        #     '/api/login/'
        # ]
        #
        # if request.path in WHITE_LIST:
        #     return

        uid = request.session.get('uid')
        print(99999999999999999)

        if not uid:
            return return_json(RET.SESSIONERR,'用户未登录')

        request.user = User.objects.get(pk=uid)

        # for k,v in request.META.items():
        #     print(k, v)

        # token = request.META.get('HTTP_X_SWIPER_AHTU_TOKEN')
        # uid = cache.get(token)
        #
        # if not uid:
        #     return render_json(code=errors.LOGIN_REQUIRED_ERR)
        #
        # request.user = User.objects.get(pk=uid)


