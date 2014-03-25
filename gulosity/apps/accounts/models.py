#!/usr/local/bin/python
# coding: utf-8

__author__ = 'wenshin'

from django.db import models
from django.contrib.auth.models import User

from gulosity.libs.models import Model


class RealUser(Model):
    SEX = (
        ('M', u'男'),
        ('F', u'女'),
        ('S', u'人妖'),
    )
    user = models.ForeignKey(User)
    name = models.CharField(verbose_name=u'姓名', max_length=20)
    sex = models.CharField(verbose_name=u'性别', max_length=5, choices=SEX)
    birthday = models.DateField(verbose_name=u'生日')
    company = models.CharField(verbose_name=u'公司', max_length=30)
    address = models.CharField(verbose_name=u'家庭地址', max_length=20)
    identity = models.CharField(verbose_name=u'身份证号码', max_length=20)
    certification = models.CharField(verbose_name=u'认证截图路径', max_length=50)
    title = models.TextField(verbose_name=u'个人主页标题')
    keywords = models.CharField(verbose_name=u'个人主页关键字', max_length=50)
    desc = models.TextField(verbose_name=u'个人主页描述')

    form_fields = ['name', 'sex', 'birthday', 'company',
                   'address', 'identity', 'certification']

    def __unicode__(self):
        return self.user.username
