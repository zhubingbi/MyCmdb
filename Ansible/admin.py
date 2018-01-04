# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.


class ToolscriptAdmin(admin.ModelAdmin):
    search_fields = ('toolname',)
    list_display = ('toolname', 'tooltype', 'comment')
    list_display_links = ('toolname',)


class PermissionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'url', 'describe')
    list_display_links = ('name',)


admin.site.register(Toolscript, ToolscriptAdmin)
admin.site.register(Permission, PermissionAdmin)

