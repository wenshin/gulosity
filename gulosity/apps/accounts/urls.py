#!/usr/bin/env python
# encoding: utf-8
# by wenshin

from django.conf.urls import patterns, url

urlpatterns = patterns('gulosity.apps.accounts.views',
    url(r'^$', 'index', name='accounts'),

    url(r'^register/?$', 'register', name='register'),

    url(r'^logout/?$', 'logout', name='logout'),

    url(r'^real-auth/?$', 'real_auth', name='real-auth'),
)


urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/?$', 'login',
        {'template_name': 'accounts/login.html'}, name='login'),
)
