# coding:utf-8
from django.db import models


class Toolscript(models.Model):
    tooltypes = (
        (0, 'shell'),
        (1, 'python'),
        (2, 'yml'),
    )

    toolname = models.CharField(max_length=255, verbose_name='工具名称',unique=True)
    toolscript = models.TextField(verbose_name='脚本',null=True, blank=True)
    tooltype = models.IntegerField(choices=tooltypes, verbose_name='脚本类型', default=0)
    comment = models.TextField(verbose_name='工具说明', null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'Toolscript'
        verbose_name = '脚本工具表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.toolname


class Permission(models.Model):
    name = models.CharField("权限名称", max_length=64)
    url = models.CharField('URL名称', max_length=255)
    argument_list = models.CharField('参数列表', max_length=255, help_text='多个参数之间用英文半角逗号隔开', blank=True, null=True)
    describe = models.CharField('描述', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ansible权限表'
        verbose_name_plural = verbose_name
        # 权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
        permissions = (
            ('addtool', '添加工具'),
            ('deltool', '删除工具'),
            ('deltools', '批量删除工具'),
            ('updatetool', '更新工具'),
            ('dotool', '执行工具'),
        )