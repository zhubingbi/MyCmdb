from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^hostlist/', hostlist),
    url(r'tools/$', tools),
    url(r'addTools/$', addtools),
    url(r'toolscript/$', toolscripts),
    url(r'^tool_script_get/(?P<shid>\d{1,3})', tools_script_get),
    #url(r'^tools-script-execute/$', tools_script_execute),
]
