from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^range/$', views.range, name='range'),
    url(r'^known/$', views.known_shutters, name='known_shutters'),
    url(r'^(?P<addr>[0-9 | A-Z|a-z]+)/add/$',views.add, name="add"),
    url(r'^(?P<name>[0-9 | A-Z|a-z]+)/sub/$',views.sub, name="sub"),
    url(r'^(?P<name>[0-9 | A-Z|a-z]+)/position/$',views.get_position, name="get_position"),
    url(r'^(?P<name>[0-9 | A-Z|a-z]+)/open/$',views.open, name="open"),
    url(r'^(?P<name>[0-9 | A-Z|a-z]+)/close/$',views.close, name="close"),
    url(r'^(?P<name>[0-9 | A-Z|a-z]+)-(?P<pos>[0-9]+)/move/$',views.set_pos, name="set_pos"),
    url(r'^test/$',views.tt, name = "tt")
]
