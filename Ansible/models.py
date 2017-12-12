# coding:utf-8
from django.db import models


class toolscript(models.Model):
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

    def __str__(self):
        return self.toolname