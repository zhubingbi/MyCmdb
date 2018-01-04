# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.


class ServersAdmin(admin.ModelAdmin):
    search_fields = ('hostname', 'ip')
    list_display = ('hostname', 'ip', 'sys', 'ctime')
    list_display_links = ('ip',)


class PermissionAdmin(admin.ModelAdmin):
    search_fields = ('url',)
    list_display = ('name', 'url', 'describe',)
    list_display_links = ('name',)


admin.site.register(Servers, ServersAdmin)
admin.site.register(ServerStatus)
admin.site.register(Permission, PermissionAdmin)