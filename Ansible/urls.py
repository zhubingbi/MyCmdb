from django.conf.urls import url
from views import *


urlpatterns = [

    url(r'tools/$', tools, name='tools'),
    url(r'addtool/$', addtool, name='addtool'),

    url(r'^tool_script_get/$', tools_script_get, name='dotool'),
    url(r'^tool_script_execute/$', tools_script_execute),
    url(r'^tool_delete/$', tool_delete, name='deltool'),
    url(r'^tools_delete/$', tools_delete, name='deltools'),
    url(r'^tool_update/$', tool_update, name='updatetool')
]
