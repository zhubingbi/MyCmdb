# coding=utf-8
from django.shortcuts import render
from models import *
from django.db.models import Q
from django.core.urlresolvers import resolve


def perm_check(request, *args, **kwargs):
    url_obj = resolve(request.path_info)
    url_name = url_obj.url_name

    if url_name:
        url_method, url_args = request.method, request.GET
        url_args_list = []
        for i in url_args:
            url_args_list.append(str(url_args[i]))
        url_args_list = ','.join(url_args_list)
        print type(url_name)
        get_perm = Permission.objects.filter(Q(url=url_name))
        if get_perm:
            for i in get_perm:
                perm_name = i.name
                perm_str = 'Ansible.%s' % perm_name
                if request.user.has_perm(perm_str):
                    return True
        else:
            return False
    else:
        return False


def check_permission(fun):
    def wapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):
            return fun(request, *args, **kwargs)
        return render(request, '403.html', locals())
    return wapper
