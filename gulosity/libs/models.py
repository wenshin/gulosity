#!/usr/local/bin/python
# coding: utf-8

__author__ = 'wenshin'

from django import forms
from django.db import models
from django.contrib import admin


class Model(models.Model):
    form_cls = None
    form_fields = []

    @classmethod
    def _init_form_cls(cls, form_fields=None):
        class Form(forms.ModelForm):
            class Meta:
                model = cls
                fields = form_fields or cls.form_fields
        return Form

    @classmethod
    def get_unbound_form(cls, fields=None):
        form_cls = cls._init_form_cls(fields)
        return form_cls()

    def get_form(self, data=None, fields=None):
        form_cls = self.__class__._init_form_cls(fields)
        return form_cls(data=data, instance=self)


class Country(Model):
    code = models.CharField(verbose_name=u'国际简码', max_length=10)
    full_name = models.CharField(verbose_name=u'全称', max_length=100)
    abbreviation = models.CharField(verbose_name=u'简称', max_length=10)

    def __unicode__(self):
        return self.abbreviation


class Province(Model):
    country = models.ForeignKey(Country, verbose_name=u'国家')
    full_name = models.CharField(verbose_name=u'全称', max_length=20)
    abbreviation = models.CharField(verbose_name=u'简称', max_length=10)

    def __unicode__(self):
        return self.abbreviation


class PostAddress(Model):
    province = models.ForeignKey(Province, verbose_name=u'省份')
    city = models.CharField(verbose_name=u'城市', max_length=30)
    district = models.CharField(verbose_name=u'区', max_length=30)
    street = models.CharField(verbose_name=u'街道', max_length=50)
    streetNumber = models.CharField(verbose_name=u'街道号', max_length=20)
    zip_code = models.IntegerField(verbose_name=u'邮政编码')

    def __unicode__(self):
        return u'%s %s %s' % (self.province.abbreviation,
                              self.city, self.street)

    form_fields = ['province', 'city', 'district',
                   'street', 'streetNumber', 'zip_code']
    form_errors = {}


class GeoLocation(Model):
    lng = models.DecimalField(verbose_name=u'经度',
                              max_digits=11, decimal_places=8)
    lat = models.DecimalField(verbose_name=u'纬度',
                              max_digits=11, decimal_places=8)

    def __unicode__(self):
        return u'经度：%s，纬度：%s' % (str(self.lng), str(self.lat))

    form_fields = ['name', 'desc', 'keywords']
    form_errors = {}


# 联系方式
class Contact(Model):
    qq = models.IntegerField(verbose_name=u'QQ号码')
    fax = models.CharField(verbose_name=u'传真', max_length=20)
    email = models.EmailField(verbose_name=u'电子邮箱')
    address = models.ForeignKey(PostAddress, verbose_name=u'邮政地址')
    telephone = models.CharField(verbose_name=u'固定电话', max_length=20)
    mobile_phone = models.IntegerField(verbose_name=u'手机号码')

    def __unicode__(self):
        return u'邮箱：%s' % (self.email)

    form_fields = ['name', 'desc', 'keywords']
    form_errors = {}


admin.site.register(Country)
admin.site.register(Province)
admin.site.register(PostAddress)
admin.site.register(GeoLocation)
admin.site.register(Contact)


# Base Class of Location Object
class SocialModel(Model):
    contact = models.ForeignKey(Contact, verbose_name=u'联系方式')
    geo = models.ForeignKey(GeoLocation, verbose_name=u'坐标')
