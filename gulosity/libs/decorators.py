#!/usr/bin/env
# coding: utf-8

from django.shortcuts import redirect

from gulosity.apps.accounts.models import UserPrivacy


def need_real_auth(func):
    def _d(req, *args, **kargs):
        real = UserPrivacy.is_user_real(req.user)
        if real:
            return func(req, *args, **kargs)
        else:
            return redirect('real-auth')
    return _d
