import os
import time

from django.core.cache import cache
from django.views.generic import View
from common.errors import *
from common.forms import ProfileForm
from common.utils import *
from common.cache_config import *
from libs import sms
from libs.https import render_json
from shopping.settings import MEDIA_ROOT
from user import logics
from user.models import User


class User_verify(View):
    def get(self,request):
        print(11111)
        return render_json()

    def post(self,request):
        """
        1.验证手机格式
        2.生成验证码
        3.保存验证码
        4.发送验证码
        :param request:
        :return:
        """
        phone_num = request.POST.get("phone_num")

        if is_phone_num(phone_num):

            #发送验证码
            if sms.send_verify_code(phone_num.strip()):

                return render_json()

            else:
                return render_json(code=SMS_CODE_ERROR)

        return render_json(code=PHONE_NUM_ERROR)

class Login(View):
    def post(self,request):
       """
       登录验证
       :param request:
       :return:
       """
       phone_num = request.POST.get("phonenum")
       code = request.POST.get("code")
       cache_code = cache.get(VERIFY_CODE_PREFIX.format(phone_num.strip()))

       if code.strip() != cache_code:

           return render_json(code=CACHE_CODE_ERROR)

       #如果存在就记录，如果不存在就创建
       user,create = User.objects.get_or_create(phonenum=phone_num)
       #设置会话机制
       request.session["uid"] = user.id

       return render_json(data=user.to_dict())

class GETProfiles(View):
    """
    提取用户信息
    """

    def post(self,request):

        user = request.user

        return render_json(data=user.profile.to_dict())

class SETProfile(View):
    """
    修改用户信息
    """
    def post(self,request):
        user = request.user
        form = ProfileForm(data=request.POST,instance = user.profile)

        if form.is_valid():
            form.save()
            return render_json()

        return render_json(data=form.errors)

class Avatar(View):
    """
    处理用户头像相关信息
    """
    def post(self,request):
        user = request.user
        avatar = request.FILES.get("avatar")
        avatar = avatar.read()
        # file_name = "avator-{}".format(int(time.time()))
        #
        # file_path = logics.upload_avator(file_name,avatar)
        # ret = logics.upload_qiniu(file_name,file_path)
        #
        # if ret:
        #     return render_json()
        # return render_json(code=QN_UPLOAD_ERROR)
        # logics.aysnc_upload_save_avatar.delay(user,avatar)
        ret = logics.upload_qiniu(avatar)
        if ret:
            return render_json()









