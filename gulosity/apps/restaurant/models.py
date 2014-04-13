#!/user/local/bin/python
# coding: utf-8

from django.db import models
from django.contrib import admin

from gulosity.apps.accounts.models import UserPrivacy
from gulosity.libs.models import Model, SocialModel


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

class KeyWord(object):
    def __init__(self, ):
        pass


class Qualification(Model):
    category = models.CharField(verbose_name=u'认证类型', max_length=50)
    source = models.CharField(verbose_name=u'资源链接', max_length=50)

    form_fields = ['category', 'source']

    def __unicode__(self):
        return u'%s %s' % (self.category, self.source)


class RestaurantPublic(SocialModel):
    owner = models.ForeignKey(UserPrivacy)
    qualifications = models.ManyToManyField(Qualification)
    keywords = models.TextField(verbose_name=u'标签')
    name = models.CharField(verbose_name=u'饭店名', max_length=50)
    slug = models.SlugField(verbose_name=u'URL地址', unique=True)
    desc = models.TextField(verbose_name=u'网页描述')
    title = models.TextField(verbose_name=u'网页标题')

    form_fields = ['name', 'desc', 'keywords']
    form_errors = {}

    def __unicode__(self):
        return self.name

    def save(self):
        self.slug = self.title = self.name
        super(RestaurantPublic, self).save()

    def is_owned_by(self, user):
        try:
            puser = UserPrivacy.objects.get(user=user)
        except:
            return False
        return True if puser.id == self.owner.id else False

    @classmethod
    def get_my_restaurants(self, user):
        try:
            puser = UserPrivacy.objects.get(user=user)
            return self.objects.filter(owner=puser)
        except:
            return []


admin.site.register(RestaurantPublic)
admin.site.register(Qualification)
