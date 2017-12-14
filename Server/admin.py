# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.


class Serveradmin(admin.ModelAdmin):
    search_fields = ('hostname', 'ip')
    list_display = ('hostname', 'ip', 'sys', 'on_line', 'ctime')
    list_display_links = ('ip',)
    list_filter = ('on_line',)


class Servers_infoadmin(admin.ModelAdmin):
    search_fields = ('ip',)
    list_display = ('ip', 'cpu_info', 'memory_info', 'disk_info', 'utime')
    list_display_links = ('ip',)
    list_filter = ('ip',)


admin.site.register(Servers, Serveradmin)
admin.site.register(Servers_info, Servers_infoadmin)