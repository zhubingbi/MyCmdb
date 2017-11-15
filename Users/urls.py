from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^addUser/', register),
    url(r'^register_phone/', register_phone),
    url(r'^listUser/', userlist),
    url(r'^modifyUser/', modifyuser),
    url(r'^modifyinput/', modifyinput),
]