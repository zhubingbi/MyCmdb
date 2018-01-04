# coding=utf-8
from django.forms import Form
from django import forms
from models import Servers


class ServersForm(forms.ModelForm):
    class Meta:
        model = Servers
        fields = '__all__'
        # exclude = ('ps',)
        # fields = [
        #    'id', 'network_ip', 'manage_ip', 'model', 'data_center', 'cabinet', 'position',
        #     'sn', 'cpu', 'memory', 'disk', 'port', 'ship_time', 'end_time', 'product_line', 'ps'
        # ]
        labels = {
            "ip": "外网IP",
        }
        widgets = {
            'ship_time': forms.DateInput(
                attrs={'type': 'date',}
            ),
            'end_time': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'ps': forms.Textarea(
                attrs={'cols': 80, 'rows': 3}
            ),
            # 'product_line': forms.SelectMultiple(
            #     attrs={'class': 'select2',
            #            'data-placeholder': ('选择产品线')}),
            # 'admin_user': forms.Select(
            #     attrs={'class': 'select2',
            #            'data-placeholder': ('Select asset admin user')}),
        }
        help_texts = {
            'ip': '必填项目,如您管理的主机无外网IP,可将内网IP输入到此。 批量执行工具都是按照此项进行操作的',
        }
        error_messages = {
            'model': {
                'max_length': ('太短了'),
            }
        }