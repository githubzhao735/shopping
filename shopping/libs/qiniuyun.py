
from qiniu import Auth,put_file,etag,put_data
from common import config
#
# def upload(file_name,file_path):
#     #构建鉴权对象
#     qn = Auth(config.QINNIU_ACCESS_KEY, config.QINNIU_SECRET_KEY)
#
#     #上传后保存的文件名
#     key = 'my-python-logo.png'
#     #生成上传 Token，可以指定过期时间等
#     token = qn.upload_token(config.QINNIU_BUCKET_NAME, file_name, 3600)
#     #要上传文件的本地路径
#
#     ret, info = put_file(token,file_name,file_path)
#
#     return ret,info

def upload(data):
    #构建鉴权对象
    qn = Auth(config.QINNIU_ACCESS_KEY, config.QINNIU_SECRET_KEY)

    #上传后保存的文件名
    # key = 'my-python-logo.png'
    #生成上传 Token，可以指定过期时间等
    token = qn.upload_token(config.QINNIU_BUCKET_NAME, None, 3600)
    #要上传文件的本地路径

    ret, info = put_data(token,None,data)
    # print(ret)
    # print("*"*100)
    # print(info)

    return ret,info






