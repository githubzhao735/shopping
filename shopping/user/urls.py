
from django.urls import path
from apis.verify_code import verify_phone_num

urlpatterns = {
    path('verify_phone/',verify_phone_num,name='verify_phone_num'),

}