
from django.urls import path
from apis.verify_code import verify_phone_num
from apis.passport import login,get_profile,set_profile,upload_avatar


urlpatterns = {
    path('verify_phone/',verify_phone_num,name='verify_phone_num'),
    path('login/',login,name='login'),
    path('get_profile/',get_profile,name='get_profile'),
    path('set_profile/',set_profile,name='set_profile'),
    path('upload_avatar/',upload_avatar,name='upload_avatar'),
}