#!/user/local/bin/python
# coding: utf-8

from django.db import models
from django.contrib import admin
from gulosity.apps.main.models import RealUser
from gulosity.libs.models import Model


# class Table(models.Model):
#     mark = models.IntegerField()
#     capacity = models.IntegerField()
#     is_idle = models.BooleanField(default=True)
#     customers = models.IntegerField()
#
#
# class Lobby(models.Model):
#     tables = models.ManyToManyField(Table)
#     manager = models.ForeignKey(User)
#
#
# class Menu(models.Model):
#     pass
#
#
# class Bill(models.Model):
#     pass
#
#
# class Finance(models.Model):
#     bill = models.ForeignKey(Bill)


class Qualification(Model):
    category = models.CharField(verbose_name=u'认证类型', max_length=50)
    source = models.CharField(verbose_name=u'资源链接', max_length=50)

    form_fields = ['category', 'source']

    def __unicode__(self):
        return u'%s %s' % (self.category, self.source)


class Restaurant(Model):
    owner = models.ForeignKey(RealUser)
    qualifications = models.ManyToManyField(Qualification)
    name = models.CharField(verbose_name=u'饭店名', max_length=50)
    desc = models.TextField(verbose_name=u'网页描述')
    title = models.TextField(verbose_name=u'网页标题')
    keywords = models.TextField(verbose_name=u'网页关键词')

    form_fields = ['name', 'qualification']

    def __unicode__(self):
        return self.name

admin.site.register(Restaurant)
admin.site.register(RealUser)