import time

from django.core.cache import cache
from common.constants import VERIFY_CODE
from common.return_json import return_json
from common.response_code import RET
from user.models import User
from common.request_method import check_request_method
from user.forms import ProfileForm
from utils.qiniuyun import upload


@check_request_method('POST')
def login(request):
    """
    通过验证码登录或注册接口
    如果手机号已存在，则登录，否则，注册

    # 1、检测验证码是否正确
    # 2、注册或登录

    :param request:
    :return:
    """
    phone_num = request.POST.get('phone', '')
    code = request.POST.get('code', '')

    phone_num = phone_num.strip()
    code = code.strip()

    cached_code = cache.get(VERIFY_CODE.format(phone_num))

    if cached_code != code:
        return return_json(RET.DATAERR,'驗證碼有誤')

    # try:
    #     user = User.obejcts.get(phonenum=phone_num)
    # except User.DoesNotExist:
    #     user = User.objects.cereate(phonenum=phone_num)

    # 如果存在 记录，则 get，否则 create
    user, created = User.objects.get_or_create(phonenum=phone_num)

    # 设置登录状态
    request.session['uid'] = user.id

    # token 认证方式
    # 为当前登录用户生成一个 token，并且存储到 缓存中，key为：token:user.id，Value为：token
    # token = user.get_or_create_token()
    # data = {'token': token}
    # return render_json(data=data)

    return return_json(RET.OK,'OK,',user.profile.to_dict())




def get_profile(request):
    user = request.user

    # return render_json(data=user.profile.to_dict(exclude=['auto_play']))
    return return_json(RET.OK,'OK',user.profile.to_dict())


def set_profile(request):
    user = request.user

    form = ProfileForm(data=request.POST, instance=user.profile)

    if form.is_valid():
        form.save()
        return return_json(RET.OK,'ok')
    else:
        return return_json(code=RET.DATAERR,msg=form.errors)


def upload_avatar(request):
    user = request.user
    avatar = request.FILES.get('avatar')

    if not avatar:
        return return_json(RET.NODATA,'數據不能爲空')

    data = avatar.read()

    file_name = 'wu-{}'.format(int(time.time()))

    ret = upload(file_name,data)

    return return_json(RET.OK,'OK')
    #
    # # 1、先将文件上传到本地服务器
    #
    # # file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    # #
    # # with open(file_path, 'wb+') as destination:
    # #     for chunk in avatar.chunks():
    # #         destination.write(chunk)
    #
    # file_path = logics.upload_avatar(file_name, avatar)
    #
    # # 2、将本地文件上传到七牛云
    # ret = logics.upload_qiniuyun(file_name, file_path)
    #
    # if ret:
    #     return render_json()
    # else:
    #     return render_json(code=errors.AVATAR_UPLOAD_ERR)
    #
    # logics.async_upload_avatar.delay(user, avatar)
    #
    # return render_json()
