# coding=utf-8
from django import forms


class AdminUserForm(forms.Form):
    phone = forms.CharField(max_length=32, label='注册电话', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user = forms.CharField(max_length=32, label='用户名称', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, label='用户密码', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='注册邮箱', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    birthday = forms.DateField(label='出生年月', widget=forms.DateTimeInput(attrs={'type': 'date'}))
    groups = forms.ChoiceField(label='业务范围', choices=[('web业务权限', 'web业务'),('数据库权限', '数据库业务'),('系统管理权限', '系统管理'),('机房运维权限', '机房运维')])
    isadmin = forms.ChoiceField(label='用户权限', choices=[('是', '管理员'),('否', '普通用户')])
    photo = forms.ImageField(label='用户头像', required=False)




