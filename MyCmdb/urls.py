"""MyCmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^index/$', index),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('Users.urls')),
    url(r'^server/', include('Server.urls')),
    url(r'^ansible/', include('Ansible.urls')),
    url(r'^interface/', include('Interface.urls')),
    url(r'^platform/', include('Platform.urls')),
]
