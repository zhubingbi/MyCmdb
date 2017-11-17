from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^hostlist/', hostlist),
    url(r'tools/$', tools),
    url(r'addTools/$', addtools),
]
