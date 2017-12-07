from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^websocket/$', websockestatus),
    url(r"^restart/$", interface_restart),
]