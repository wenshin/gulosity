from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('gulosity.apps.main.views',
    url(r'^$', 'index', name='index'),
)


urlpatterns += patterns('',
    url(r'^restaurant/', include('gulosity.apps.restaurant.urls')),
    url(r'^accounts/', include('gulosity.apps.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
