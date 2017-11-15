from django.conf.urls import url
from views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^saveServer/', saveServer),
    url(r'^serverlist/', serverlist),
    url(r'^serverlist/(?P<number>\d{1,3})', serverlist),

    url(r'^doCommand/', doCommand),
    url(r'^exec/exec_cmd/', exec_cmd),
    url(r'^serverConnect', serverConnect),
    url(r'^gateone', gateone),
    url(r'^upload', upload),
]
