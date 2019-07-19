from django.urls import path

from social import apis

urlpatterns = [

    path("recommence/",apis.recommence,name="recommence"),
    path("like/",apis.like,name="like"),

]





