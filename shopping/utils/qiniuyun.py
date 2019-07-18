from qiniu import Auth,put_data,etag,urlsafe_base64_encode
import qiniu.config

def upload(file_name,data):

    # print(data)
    """
    本地文件上传至七牛云
    :param file_name:
    :param file_path:
    :return:
    """
    # 七牛云存储配置
    access_key = '9M_4LVjxHubwJP2yaT_uJTyeWJI-f9ct7zo3hVIG'
    secret_key = 'KmfZX-JrW-Bj36R-5fjHAK_7AOTzTqnfsKFC1HMn'
    bucket = 'shopping'
    scheme = 'http'
    # scheme_hosts = 'http://putktasgp.bkt.clouddn.com'
    # 构建鉴权对象
    q = Auth(access_key,secret_key)

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket=bucket)

    ret, info = put_data(token,None,data)

    return ret, info
