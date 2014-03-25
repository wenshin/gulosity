#!/usr/local/bin/python
# coding: utf-8

__author__ = 'wenshin'

from django import forms
from django.db import models


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