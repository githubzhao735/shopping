import os
import time
from urllib.parse import urljoin

from common import config
from libs import qiniuyun
from shopping.settings import MEDIA_ROOT
from worker import celery_app


def upload_avator(file_name,avatar):
    """
    下载图片到本地
    :param file_name:
    :param avatar:
    :return:
    """
    file_path = os.path.join(MEDIA_ROOT,file_name)
    with open(file_path,"wb+") as f:
        for chunk in avatar.chunks():
            f.write(chunk)
    return file_path


def upload_qiniu(data):
    """
    上传图片到七牛云
    :param file_name:
    :param file_path:
    :return:
    """

    ret,info = qiniuyun.upload(data)
    return True if info.status_code ==200 else False


@celery_app.task
def aysnc_upload_save_avatar(user,avatar):
    """
    异步上传头像到七牛云并且保存路径到数据库
    :param user:
    :param avatar:
    :return:
    """
    file_name = "avator-{}".format(int(time.time()))
    file_path = upload_avator(file_name,avatar)

    # upload_avator(file_name,avatar)

    ret = upload_qiniu(file_name,file_path)
    if ret:
        user.avatar = urljoin(config.QINNIU_HOST,file_name)
        user.save()










