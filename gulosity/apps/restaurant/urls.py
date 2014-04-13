from django.conf.urls import patterns, url


urlpatterns = patterns('gulosity.apps.restaurant.views',
    url(r'^$', 'index', name='restaurant-index'),
    url(r'^/?new/?$', 'new', name='restaurant-new'),
    url(r'^name/(?P<slug>[a-zA-Z0-9\-]{1,50})/?', 'page', name='restaurant-page'),
)
