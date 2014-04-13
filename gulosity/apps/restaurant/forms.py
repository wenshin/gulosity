#!/usr/local/bin/python
# coding: utf-8

from django import forms

from models import RestaurantPublic


class RestaurantPublicFrom(forms.ModelForm):
    name = forms.CharField(label=u'餐馆名')

    class Meta:
        model = RestaurantPublic
        fields = ('name',)