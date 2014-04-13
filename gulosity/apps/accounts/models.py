#!/usr/local/bin/python
# coding: utf-8

__author__ = 'wenshin'

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from gulosity.libs.models import SocialModel


class UserPrivacy(SocialModel):
    SEX = (
        ('M', u'男'),
        ('F', u'女'),
    )
    sex = models.CharField(verbose_name=u'性别', max_length=5, choices=SEX)
    user = models.ForeignKey(User)
    name = models.CharField(verbose_name=u'姓名', max_length=20)
    desc = models.TextField(verbose_name=u'个人主页描述')
    title = models.TextField(verbose_name=u'个人主页标题')
    address = models.CharField(verbose_name=u'家庭地址', max_length=20)
    company = models.CharField(verbose_name=u'公司', max_length=30)
    birthday = models.DateField(verbose_name=u'生日')
    identity = models.CharField(verbose_name=u'身份证号码', max_length=20)
    keywords = models.CharField(verbose_name=u'个人主页关键字', max_length=50)
    certification = models.CharField(verbose_name=u'认证截图路径', max_length=50)

    form_fields = ['name', 'sex', 'birthday', 'company',
                   'address', 'identity', 'certification']

    def __unicode__(self):
        return self.user.username

    @classmethod
    def is_user_real(cls, user):
        user_private = cls.objects.filter(user=user)
        return True if user_private else False


admin.site.register(UserPrivacy)
