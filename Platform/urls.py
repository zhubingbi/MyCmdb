from django.conf.urls import url
from views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'login_logs/', login_logs),
    url(r'server_logs/', server_logs),
]