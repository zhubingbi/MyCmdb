from django.conf.urls import url
from views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^saveserver/$', saveserver, name='saveserver'),


    url(r'^doCommand/', doCommand),
    url(r'^exec/exec_cmd/', exec_cmd),
    url(r'^serverConnect', serverConnect),
    url(r'^gateone', gateone),

    url(r'^serverlist/$', serverlist, name='serverlist'),
    url(r'^serverinfo/$', serverinfo, name='serverinfo'),
    url(r'^serverupdate/$', serverupdate, name='serverupdate'),
    url(r'^serverstatus/$', serverstatus, name='serverstatus'),
]
