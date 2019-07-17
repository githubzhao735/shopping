from django.utils.deprecation import MiddlewareMixin

from common import errors
from libs.https import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):

        URL_LIST = [
            "/apis/user/login/",
            "/apis/user/user_verify/",
        ]

        if request.path in URL_LIST:
            return
        uid = request.session.get("uid")
        if not uid:
            return render_json(code=errors.LOGIN_REQUIRED_ERROR)

        request.user = User.objects.get(pk=uid)


