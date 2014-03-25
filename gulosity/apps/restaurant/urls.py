from django.conf.urls import patterns, include, url


urlpatterns = patterns('gulosity.apps.restaurant.views',
    url(r'^$', 'index', name='restaurant-index'),
    url(r'^(?P<restaurant_name>[a-zA-Z\-])/?', 'index', name='restaurant'),
    url(r'^add/?$', 'add', name='restaurant-add'),
)