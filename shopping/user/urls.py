from django.urls import path
from user import apis
urlpatterns = [

    path("user_verify/",apis.User_verify.as_view(),name="user_verify"),
    path("login/",apis.Login.as_view(),name="login"),
    path("get_profile/",apis.GETProfiles.as_view(),name="get_profile"),
    path("set_profile/",apis.SETProfile.as_view(),name="set_profile"),
    path("avatar/",apis.Avatar.as_view(),name="avatar"),

]



