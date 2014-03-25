#!/usr/bin/env python
# encoding: utf-8
# by wenshin

from django.conf.urls import patterns, url

urlpatterns = patterns('gulosity.apps.accounts.views',
    url(r'^$', 'index',
        {'template_name': 'accounts/index.html'}, name='accounts'),

    url(r'^register/?$', 'register',
        {'template_name': 'accounts/register.html'}, name='register'),

    url(r'^logout/?$', 'logout', name='logout'),

    url(r'^real-auth/?$', 'real_auth',
        {'template_name': 'accounts/real_auth.html'}, name='real-auth'),
)


urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/?$', 'login',
        {'template_name': 'accounts/login.html'}, name='login'),
)
