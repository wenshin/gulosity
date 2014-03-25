#!/usr/local/bin/python
# coding: utf-8

from django import forms

from models import Restaurant


class RestaurantFrom(forms.ModelForm):
    name = forms.CharField(label=u'餐馆名')

    class Meta:
        model = Restaurant
        fields = ('name',)