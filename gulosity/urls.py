from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('gulosity.apps.main.views',
    url(r'^$', 'index', name='index'),
    url(r'^accounts/logout/?$', 'logout', name='logout'),
    url(r'^accounts/register/?$', 'register', {'template_name': 'register.html'}, name='register'),
    url(r'^accounts/real-auth/?$', 'real_auth', {'template_name': 'real_auth.html'}, name='real-auth'),
)


urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/?$', 'login', {'template_name': 'login.html'}, name='login'),
)


urlpatterns += patterns('',
    url(r'^restaurant/', include('gulosity.apps.restaurant.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
